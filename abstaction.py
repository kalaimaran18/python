from abc import ABC , abstractmethod

class Family(ABC):
    @abstractmethod

    def dad(self):
        print("he is poor")
    @abstractmethod

    def childrens(self):
        print("they are playing games")

class Village(Family):
    
    def dad(self):
        print("He is poor")
    
    def childrens(self):
        print("They are playing games")
c=Village()
c.childrens()
c.dad()
c.childrens()