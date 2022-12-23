#Miscellaneous
#Load Data from File
import numpy as np
filedata = np.genfromtxt('data.txt', delimiter=',')
print(filedata)#automatically float type 
filedata = filedata.astype('int32')
print(filedata)
