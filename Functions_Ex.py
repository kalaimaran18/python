# Find out the Odd or Even Number using Function.
# Question 1

def Num():
    a=int(input())
    if a%2==0:
        print("Even Number")
    else:
        print("Odd Number")

Num()


# Same as the Problem using Function to Identify Pass or Fail.
# Question 2

def Num1():
    a=int(input())
    if a%2==0:
        print("Even Number")
    else:
        print("Odd Number")

Num1()



# Identify the Range function Method.
# Question 3

def printrange(a,b):
    for i in range(a,b):
        print(i,end=" ")

printrange(1,11)