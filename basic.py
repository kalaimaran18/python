'''
# to find a num is magic number or not 
number=int(input("enter a number"))
temp=number
sum_digits=0
product_digits=1

#while loop 
while temp>0:
    digit=temp%10
    sum_digits+=digit
    product_digits*=digit
    temp=temp//10
if sum_digits==product_digits:
    print(number,"is a magic number :")
else:
    print(number,"is not a magic number 123:")

    '''
'''
# at the same problem of above

sum,mul=0,1
while (n>0):
    r=n%0
    sum=sum+r
    mul=mul*r
    n=n//10
if sum==mul:
    print("magic number")
else:
    print("not a magic number")
'''
'''
#oops concept(class and object)

class student:
    def say_hello(self):
        print("hi,i'm a student")   
s1=student()
s1.say_hello()

'''
'''
#constructors
class students:
    def __init__(self,fname,age):
        self.x=fname
        self.y=age


    def display(self):
        print(f"name:{self.x},age:{self.y}")
s1=students(fname="kalai",age=20)
s1.display()
'''
'''

# single level inheritance
class bcci:
    def ipl(self):
        print(" control of bcci")

    def tnpl(self):
        print("under control of bcci")
t=bcci()
t.ipl()
t.tnpl()

'''
'''
#multi level inheritance
class students:
    def cse(self):
      print("average of students")

    def civil(cse):
      print("better to study ")
f=students()
f.cse()

'''
'''
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
         
o=dad()
o.house()
o.agriland() 
o.his_son()
o.his_wife() 

'''
'''
# prime number program
num=int(input("enter the number:"))
if num<=1:
    print("not a prime")
else:
    is_prime =True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print("prime number")
    else:
        print("not a prime")
'''

#access specifier
class parent:
    def __init__(self):
        self.public="kalai"
        self._protect=1234
        self.__private="private"
        print("amazing:",self.public)
        print("roll number:",self._protect)
        print("this is my:",self.__private)
a=parent()
