import numpy as np

#numpy using in where() method
o=np.array([7,4,9,2,8,4,1])
c=np.where(o==4)
print(c)

#numpy using where()method
v=np.array([4,8,0,7,6,1,2,5,6,6,6])
b=np.where(v==6)
print(b)

#numpy using where() even method
k=np.array([7,6,9,3,2,0])
m=np.where(k%2==0)
print(m)

#numpy using odd  method
x=np.array([3,6,9,0,1,6,4,7])
a=np.where(x%2==1)
print(a)

#numpy using in searchsort() method
g=np.array([4,6,9,9,8,8,3,2,5])
d=np.searchsorted(g,8)
print(d)

#numpy using searchsort() method
c=np.array([5,9,4,2,7,5,8])
l=np.searchsorted(c,8,side='right')
print(l)

#numpy using searchsort()method
u=np.array([6,4,2,9,80,7])
h=np.searchsorted(u,[6,5,8])
print(h)