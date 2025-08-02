import numpy as np

#numpy join method
v=np.array([[1,3,5,6],[6,9,8,2]])
c=np.array([[3,3,7,0],[2,8,9,5]])
x=np.concatenate((v,c))
print(x)

#numpy join in 2D array
d=np.array([[4,8,5],[3,6,7]])
h=np.array([[3,6,5],[7,3,8]])
b=np.concatenate((d,h),axis=1)
print(b)

#numpy join in stack method

d=np.array([4,8,5])
h=np.array([3,6,5])
f=np.stack((d,h),axis=1)
print(f)

#numpy join in vstack (coloum based)

d=np.array([4,8,5])
h=np.array([3,6,5])
g=np.vstack((d,h))
print(g)

#numpy join in hstack (row based)

d=np.array([4,8,5])
j=np.array([3,6,5])
a=np.hstack((d,h))
print(a)

#numpy join in dstack (height based)
s=np.array([4,8,5])
k=np.array([3,6,5])
t=np.dstack((d,h))
print(t)
