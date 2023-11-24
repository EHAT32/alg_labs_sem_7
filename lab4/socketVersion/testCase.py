import multiprocessing
from linServer import ServerLinear
from client import *
from threadServer import ServerTread_cv
from newProcessServer import ProcessServer

def createServer():
    server = ProcessServer()
    server.run_server()
    print('server is running')
    
def createClients():
    clients = []
    start = time.time()
    for i, purpose in enumerate(PURPOSES):
        clients.append(threading.Thread(target=generate_client, args=(i, purpose), daemon=False))
        clients[i].start()
        # print(f'client {i} appeared')

    for client in clients:
        client.join()
    print('client finished')
    print(f'Serve time: {int(time.time() - start)} seconds')


if __name__ == '__main__':
    serverProcess = multiprocessing.Process(target=createServer)
    clientProcess = multiprocessing.Process(target=createClients)
    serverProcess.start()
    clientProcess.start()
    clientProcess.join()
    serverProcess.join()