# Accessing/Changing specifi elements,rows,columns,etc

import numpy as np
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

a.shape

#Get a specific element[r,c]
a[1,5]

a[1,-2]


#Get a specific row
a[0,:]

#Get a specific column
a[:,2]

#get a little more fancy[startindex:endindex:stepsize]
a[0,1:6:2]


#get a little more fancy[startindex:endindex:stepsize]
a[0,1:-2:2]


#updating 
a[1,5] = 20
print(a)


a[:,2] = [1,2] #column 2 all 5
print(a)
