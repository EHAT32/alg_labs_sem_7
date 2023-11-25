from serverModel import *

clientIds = [1, 2, 10, 11, 2]
clients = [Client(id) for id in clientIds]
testServer = Server()

testServer.addClients(clients)
testServer.showAllClients()
testServer.signUpClients([1, 10, 11, 1])
testServer.showAllClients()

def funny():
    print('eee')

def funny2():
    print('vvvv')

testServer.addTask(funny)
testServer.addTask(funny2)

for task in testServer.pool:
    task()
