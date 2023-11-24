import asyncio
from datetime import datetime
from server import Server 

request_map = Server.request_map

counter = 0

class AsyncServer(Server):
    def __init__(self, host, port) -> None:
            self.host = host
            self.port = port
            super().__init__()

    async def run_server(self):
        server = await asyncio.start_server(self.serve_client, self.host, self.port)
        await server.serve_forever()


    async def serve_client(self, reader, writer):
        global counter
        cid = counter
        counter += 1
        print(f'Client {cid} connected - {datetime.now().time()}')
        request = await reader.read(1024)
        response = await self.handle_request(request)
        writer.write(response)
        await writer.drain()
        writer.close()
        print(f'Client {cid} served - {datetime.now().time()}')


    async def handle_request(self, request):
        if not (request in request_map.keys()):
            return b"failed"
        await asyncio.sleep(request_map[request][1])
        return b"served"

if __name__ == '__main__':
    server = AsyncServer('127.0.0.1', 9090)
    asyncio.run(server.run_server())