#logarithmicနည်းအရ increment လုပ်ပြမှာ
## Logarithmic sequences
import numpy as np
arrObj = np.logspace(0,2,5)#10 to the power 0,10 to the power 2,0 နဲ့ 100  ကြားက ၅လုံးထွက်လာမှာဖြစ်တယ်
print(arrObj)

#mesh grid
#1 dimensional coordinate array to multi dimensional coordinate array တွေအဖြစ်ပြောင်းချင်လျှင်သုံးတယ်
#rectangular grid ပုံစံမျိုးကိုဆိုလိုခြင်းဖြစ်တယ်


x = np.array([-1,0,1])
y = np.array([-2,0,2])
X,Y = np.meshgrid(x,y)
print(X)#row style
print(X.shape)
print(Y)#col style
print(Y.shape)
print(X.ndim)
print(Y.ndim)

Z = (X+Y)**2
print(Z)


#logathmic sequence
arrObj = np.logspace(0,2,5)#
print(arrObj)
