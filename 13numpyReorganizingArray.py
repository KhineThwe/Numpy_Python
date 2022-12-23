#reorganizing arrays
import numpy as np
before = np.array([[1,2,3,4],[5,6,7,8]])
before
print(before.shape)

# after = before.reshape((8,1))
# print(after)

after = before.reshape((2,2,2))
print(after)
