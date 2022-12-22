import numpy as np

#3d example
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

#Get a specific element(work outside in)
b[0,1,0]

#get all element's second row
b[:,1,:]
b[:,0,:]


#replace
b[:,1,:] = [[9,9],[8,8]]
print(b)
