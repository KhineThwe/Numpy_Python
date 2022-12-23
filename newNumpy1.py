import numpy as np
arr = np.array([
    [1,2,3]
    ,[4,5,6]
    ,[7,8,9]
])
#empty takes 3 arg ---> shape,dtype and order ka Col or row
#C ---> contiguous layout(row - major order)#အစဉ်လိုက်ရှိလို့ Index တွေနဲ့ access လုပ်လို့ရ
#F ---> fortran layout (col - major order)
#A ---> any order
#K ---> Keep order
print(arr[0])
print(arr.ndim)#rol col ရှိလို့ 2D array
#3D array
arr1 = np.arange(8)
print("First stage array: ",arr1)
print("Dimension of arr: ",arr1.ndim)
#to create 1 D to 2D
arr2D = arr1.reshape(2,4)#row col
print(arr2D)
print("Dim of arr2D : ",arr2D.ndim)
#array 1 ခုထဲကို 2 depth လို့ခေါ်
#2D array ထဲကို 2D ပေါင်းထည့်တာကို 3D array လို့ခေါ်တယ်
#1+1 = 2depth (3 dimension)
#3d
arr3D = arr1.reshape(2,2,2)#last 2 = depth
print(arr3D)
print("Dim of arr3D : ",arr3D.ndim)



