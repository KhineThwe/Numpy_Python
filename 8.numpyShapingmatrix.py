import numpy as np
output = np.ones((5,5))
print(output)

z= np.zeros((3,3))
print(z)

z[1,1] = 9
print(z)

output[1:4,1:4] = z #first row to 3 rd row and first col to second col 
print(output)

#or
output[1:-1,1:-1] = z #first row to 3 rd row and first col to second col 
print(output)
