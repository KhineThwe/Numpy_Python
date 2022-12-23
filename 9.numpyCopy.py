import numpy as np
a = np.array([1,2,3])
print(a)

#be careful when copying arrays
b = a
b
b[0] = 100
b

#issue
a
#because we are not telling numpy to copy that element that's why b still pointing a
#to solve that problem,we need to tell numpy ---> copy
b = a.copy()
b[0] = 100
b
a
