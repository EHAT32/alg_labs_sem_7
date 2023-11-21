class Client:
    def __init__(self, id : int) -> None:
        self.id = id
        self.signedUp = False
        
    def isSignedUp(self) -> bool:
        return self.signedUp