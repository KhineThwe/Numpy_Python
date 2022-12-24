#full_like က လုံးဝ clone ဟွးလိုက်တာ
import numpy as np
x = np.array([-1,0,1])
y = np.array([-2,0,2])
X,Y = np.meshgrid(x,y)
def full(inarray):
    newarr = np.full_like(inarray,11)#ဝင်လာမဲ့ array နဲ့ထည့်ရမဲ့ data နှစ်ခုပါရမယ်
    #newarr = np.ones_like(inarray)
    #newarr = np.empty_like(inarray)
    return newarr

full(X
     
     
     
#Identity
idenArray = np.identity(3)#diagonal တစ်လျှောက်မှာပဲ 1 တွေပါမှာဖြစ်တယ် #float အနေနဲ့ပြပေးတယ် 1 ka float type anay nae pr dal
idenArray


#eye
eyeArray = np.eye(4,k=2)
eyeArray
     
#Custom diagonal
x = np.arange(0,20,5)
x
#diArray = np.diag(x)
diArray = np.diag(x,k=1)#row col extend auto lote pay tal
diArray = np.diag(x,k=-3)
diArray
