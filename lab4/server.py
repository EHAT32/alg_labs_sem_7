from client import Client
from typing import List

class Server:
    def __init__(self) -> None:
        self.clients = {}
        self.pool = []
        
    def addClient(self, client : Client) -> None:
        if client.id in self.clients:
            print(f'Client {client.id} is already here!')
            return
        else:
            self.clients[client.id] = client
        
    def addClients(self, clients : List[Client]) -> None:
        for client in clients:
            self.addClient(client)
            
    #activity
    def signUpClients(self, ids : List[int]) -> None:
        for clientId in ids:
            client = self.clients[clientId]
            if client.isSignedUp:
                print(f'Client {clientId} is already signed up!')
            else:
                client.isSignedUp = True
                
    def showSignedUpClients(self) -> None:
        for client in self.clients.itervalues():
            if client.isSignedUp:
                print(f'Client {client.id}')
                
    def showAllClients(self) -> None:
        for client in self.clients.values():
            print(f'Client {client.id} signed up: {client.isSignedUp}')
            
    def showMainPage(self) -> None:
        print('There it is, watch it')