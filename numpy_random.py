from numpy import random
#using integer value random
o=random.randint(254)
print(o)

#Float value
r=random.rand(3)
print(r)

#integer value with size
u=random.randint(34,size=(2,4))
print(u)

#Float value with size
c=random.rand(4,3)
print(c)

#integer value with choice
f=random.choice([50,34,67,81,49])
print(f)

#float value with choice
v=random.choice(5,7)
print(v)

#random choice with size
b=random.choice([3,5,7,0,8],size=(3,2))
print(b)