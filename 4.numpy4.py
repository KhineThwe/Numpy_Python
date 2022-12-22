# import numpy as np
a = np.array([1,2,3],dtype='int16') 
print(a)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

#Get dimension
a.ndim

#Get shape
#to get row and column
b.shape

#Get type #by default ---> int32
a.dtype


#Get Size#we will get in bytes
a.itemsize
b.itemsize


#get total size
a.size*a.itemsize


#or get total size
a.nbytes
