from client import Client
from typing import List

class Server:
    def __init__(self) -> None:
        self.clients = []
        self.pool = []
        
    def addClient(self, client : Client) -> None:
        self.clients.append(client)
        
    def addClients(self, clients : List[Client]) -> None:
        for client in clients:
            self.addClient(client)