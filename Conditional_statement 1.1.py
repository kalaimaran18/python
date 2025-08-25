#Conditional statement problem solving using python 

#Find largest three number

a=int(input())
b=int(input())
c=int(input())
if a>b:
    print(a)
elif b>c:
    print(b)
elif a>c:
    print(a)
else:
    print(c)

#Number range validation 32 to 65

num=int(input())
if num>=32 and num<=65:
    print("Inside the Range")
else:
    print("Outside of the Range")

#Leap year or Not

year=int(input())
if year%4==0 and year%100!=0 or year%400==0:
    print("Leap Year",year)
else:
    print("Not a leap year",year)


# Pass Fail and Distinction

mark=int(input())
if mark>=40 and mark<80:
    print("PASS")
elif mark>=80 and mark<=100:
    print("DISTINCTION")
else:
    print("FAIL")