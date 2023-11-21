from client import Client
from typing import List

class Server:
    def __init__(self) -> None:
        self.clients = {}
        self.pool = []
        
    def addClient(self, client : Client) -> None:
        if self.clients[client.id] is not None:
            print('Client is already here!')
            return
        else:
            self.clients[client.id] = client
        
    def addClients(self, clients : List[Client]) -> None:
        for client in clients:
            self.addClient(client)
            
    #activity
    def signUpClient(self, ids : List[int]) -> None:
        for clientId in ids:
            client = self.clients[clientId]
            if client.isSignedUp():
                print(f'Client {clientId} is already signed up!')
            else:
                client.signedUp = True