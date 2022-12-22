# Initializing Different Types of Arrays
import numpy as np


#All 0s matrix
np.zeros(5)

np.zeros((2,3))#2*3 matrix

np.zeros((2,3,3))#2*3 matrix 3 dimensional


#All ones matrix
np.ones(5)
np.ones((2,3))
np.ones((4,2,3))
np.ones((4,4,2,3))


#Any other nummber
np.full((2,2),99)
#takes two parameter --> shape and value


np.full((2,2),99,dtype='float32')
#takes two parameter --> shape and value and dtype is optional

# c= np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
np.full_like(c,4)


#Random decimal numbers
np.random.rand(4,2)
#shape 


np.random.rand(4,2,3)
#shape 


#Random decimal numbers
np.random.random_sample(c.shape)
#if u want to use shape use random_sample


#random interger values
np.random.randint(7,size = (3,3))


#random interger values
np.random.randint(4,8,size = (3,3))


np.identity(3)

np.identity(5)


arr = np.array([1,2,3])
r1 = np.repeat(arr,3)
print(r1)

arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis = 0)
print(r1)

#repeat an array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis = 0)
print(r1)
