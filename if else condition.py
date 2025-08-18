# Odd or even problem

o=int(input())
if o%2==0:
    print("even")
else:
    print("odd")

# If a number positive or negative or zero

t=int(input())
if t>0:
    print("positive")
elif t==0:
    print("zero")
else:
    print("negative")

# Largest of two numbers

a=int(input())
v=int(input())
if a>v:
    print(a)
else:
    print(v)
    
# Largest of three numbers

i=int(input())
b=int(input())
m=int(input())
if i>b and i>m:
    print(i)
elif b>m and i<b:
    print(b)
else:
    print(m)