import numpy as np

#numpy using shape
arr=np.array(['2','5','7','9','6','2','9','3'])
print(arr.shape)

n=np.array([['2','5','7'],['1','9','6']])
print(n.shape)
 
 #numpy using reshape

c=np.array(['2','5','7','9','6','2','9','3'])
n=c.reshape(2,4)
print(n)

c=np.array(['2','5','7','9','6','2','9','3'])
b=c.reshape(2,4,-1)
print(c)

c=np.array(['2','5','7','9','6','2','9','3'])
b=c.reshape(2,4,-2)
print(c)

#Iterate method using numpy

x=np.array([2,4,5,6,7,8,9])
for i in x:
    print(x)

#Iterate method using two loops
x=np.array([[2,4,5,6],[7,3,8,9]])
for i in x:
    for y in i:
        print(y)


#using numpy in reshape
u=np.array(['3','65','43','28'])
c=u.reshape(2,2)
print(c)

