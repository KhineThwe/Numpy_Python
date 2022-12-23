import numpy as np
arr = np.zeros((3,3),dtype=int)#default C type  ---> p.zeros(shape,type,'C')
print(arr)
#takes 3 para


one = np.ones((3,3),dtype=float)
print(one)


#asarray = routine

#myList = [1,2,3,4,5,6,7,8,9]
#print(type(myList))
myList = (1,2,3,4,5,6,7,8,9)
print(type(myList))
npArray = np.asarray(myList)
print(npArray)
print(type(npArray))
