import numpy as np
arr = np.array([
    [1,2,3],[4,5,6],[7,8,9]
])
print(arr[0])
print(type(arr))
a = np.array([1,2,3])
b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
c = np.array([[(1.5,2,3), (4,5,6)],[(3,2,1), (4,5,6)]], dtype = float)
print(a)
print(b)
print(c)
numZero = np.zeros((3,4))
print(numZero)
