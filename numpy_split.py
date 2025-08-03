import numpy as np

#numpy with using split()
r=np.array([3,5,6,7])
b=np.array_split(r,2)
print(r) 

#numpy with split()

b=np.array([[3,5,7],[4,9,1]])
m=np.array_split(b,2)
print(m)

#numpy with split(2D array)

b=np.array([[3,5,7],[4,9,1]])
m=np.array_split(b,2,axis=1)
print(m)

#numpy using hsplit()

b=np.array([[3,5,7],[4,9,1],[6,4,2],[8,0,5],[3,7,1],[3,8,1]])
s=np.hsplit(b,3)
print(s)

#numpy using split()
b=np.array([[3,5,7],[4,9,1],[6,4,2],[8,0,5],[3,7,1],[3,8,1]])
s=np.array_split(b,3,axis=1)
print(s)

#numpy using vstack()

c=np.array([[3,7,0],[6,2,1]])
m=np.array_split(c,2)
print(m)
