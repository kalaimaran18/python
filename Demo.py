#Python local variable

def game():
    sports="cricket"
    print("I love",sports)
game()


#Enclosing nested variable 
 
def card():
    discount=10
    def checkout():
        print("applying discount:",checkout)
    checkout()
card()


#global variable in python 

peri_college="students"
def hostel():
    print("more than 500",peri_college)
def dayscholar():
   print("more than 300",peri_college)
hostel()
dayscholar()

#type casting 

x="focus"
v=int("356")
d=23
f=float("235")
print(type(x))
print(type(d))
print(type(v))
print(type(f))


# string handling and string manipulation
name = "kalAi"
print(name.lower())
print(name.upper())
print(name.capitalize())


# formatted string value and string handling
name = "victory"
age= "35"
print(f"{name} and  {age}")


# list in python 
favourate_food=['pizza','burger','idly','dosa','poori']
favourate_food[2]="chicken"
print(favourate_food)


# mixed list
mixed=("kalai",23,27.5)
for a in mixed:
    print(a)
    
#Enumurate function 

Au_college=['jpr','peri','skp','arunai','sairam','madha']
for i,location in enumerate(Au_college):
    print(f"location {i}: {location}")


#tuple
cse_a=('kalai','dhinesh','kawin','bharath','periyanna','idris','prajan','kalai')
for k in cse_a:
    print(k)
    print(cse_a.count('kalai'))
    print(len(cse_a))
    print(cse_a[4])
    print(cse_a[0:5])

#set in python 

char={'v','t','f','s','u','a','f','c','d','s','t'}
spec_char=set(char)
print(spec_char)


# Oops concept(class and object)

class student:
    def say_hello(self):
        print("hi,i'm a student")   
s1=student()
s1.say_hello()

#constructors
class students:
    def __init__(self,fname,age):
        self.x=fname
        self.y=age


    def display(self):
        print(f"name:{self.x},age:{self.y}")
s1=students(fname="kalai",age=20)
s1.display()

# single level inheritance
class bcci:
   def tnpl(self):
        print("under control of state ")
t=bcci()
t.ipl()
t.tnpl()


#multi level inheritance
class students:
    def cse(self):
      print("average of students")

    def civil(cse):
      print("better to study ")
f=students()
f.cse()
f.civil()

#polymorphism
class dad:
    def house(self):
         print("house white")
    def agriland(self):
         print("greenish")
    def his_wife(self):
         print("tailor")
    def his_son(self):
         print("computer engineer")
         
    def his_wife(self):
        print("teacher")
o=dad()
o.house()
o.agriland() 
o.his_son()
o.his_wife() 

#abstraction methosds

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
c.dad()
c.childrens()
