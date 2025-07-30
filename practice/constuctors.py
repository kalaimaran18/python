#constructors
# create class book

class book:
    def __init__(self,author,title):
        self.x=author
        self.y=title
    def display(self):
        print(f"{self.x} and  {self.y}")
s1=book(author="guido van rosham", title="python")
s1.display()
    
    #instruction 
class college:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display(self):
        print(f"College Name: {self.name}, Location: {self.location}")
s2 = college(name="ABC College", location="New York")
s2.display()