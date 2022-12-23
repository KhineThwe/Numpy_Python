import numpy as np
#Boolean Masking and Advanced Indexing
filedata = np.genfromtxt('data.txt', delimiter=',')
print(filedata)#automatically float type 
filedata = filedata.astype('int32')

filedata > 50
filedata[filedata > 50]

#you can index with a list in numpy
# a = np.array([1,2,3,4,5,6,7,8,9,10])
# a[[1,2,8]]

np.any(filedata > 50,axis=0)
np.all(filedata > 50,axis=0)

(((filedata > 50) & (filedata < 100)))


(~((filedata > 50) & (filedata < 100)))
