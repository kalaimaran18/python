import numpy as np

#creating numpy
#n1=np.array([0,2,4,5])
#print(n1)
# 2d array
n2=np.array([[1,2,3,4],[0,6,5,7]])
print(n2)

# creating zeros
n3= np.zeros([2,4,2])
print(n3)

# numpy ones
n4=np.ones([3,4,2])
print(n4)

# copy and view
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr= np.concatenate((arr1,arr2))
print(arr)

#join 2d arrays along rows
arr1=np.array([[3,4],[6,0]])
arr2=np.array([[7,8],[2,1]])
arr=np.concatenate((arr1,arr2),axis=1)
print(arr)


#stck methon array

arr=np.array([1,2,3,4])
arr1=np.array([5,6,7,8])
arr2=np.stack((arr,arr1),axis=1)
print(arr2)

#array_split

arr1=np.array([0,2,4,5,6,7,8,9,1])
newarr=np.array_split(arr1,4)
print(newarr[0])
print(newarr[1])
print(newarr[2])
print(newarr[3])