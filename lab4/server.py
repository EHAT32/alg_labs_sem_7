from client import Client
from typing import List
import time

class Server:
    def __init__(self) -> None:
        self.clients = {}
        self.pool = [function]
        
    def addClient(self, client : Client) -> None:
        if client.id in self.clients:
            print(f'Client {client.id} is already here!')
            return
        else:
            self.clients[client.id] = client
        
    def addClients(self, clients : List[Client]) -> None:
        for client in clients:
            self.addClient(client)
            
    def addTask(self, task : function) -> None:
        self.pool.append(task)
        
    def addTasks(self, tasks : List[function]) -> None:
        for task in tasks:
            self.addTask(task)
            
    #activity
    def signUpClient(self, id : int) -> None:
        client = self.clients[id]
        if client.isSignedUp:
            print(f'Client {id} is already signed up!')
        else:
            client.isSignedUp = True
    
    def signUpClients(self, ids : List[int]) -> None:
        for id in ids:
            self.signUpClient(id)
                
    def showSignedUpClients(self) -> None:
        for client in self.clients.itervalues():
            if client.isSignedUp:
                print(f'Client {client.id}')
                
    def showAllClients(self) -> None:
        for client in self.clients.values():
            print(f'Client {client.id} signed up: {client.isSignedUp}')
            
    def showMainPage(self) -> None:
        showPageSleepTime = 1
        print('There it is, watch it')
        time.sleep(showPageSleepTime)