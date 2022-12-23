###Linear algebra
a = np.ones((2,3))
a

b = np.full((3,2),2)
b

#a*b#ValueError

#use matmul
np.matmul(a,b)

#find the determinant
c = np.identity(3)
np.linalg.det(c)

#futher info --> https://numpy.org/doc/stable/reference/routines.linalg.html
