#Array တစ်ခုထဲမှာ နောက်ထပ် dimensions တွေ add ဖို့ newaxis တင်မဟုတ်ဘဲ
#အခြားသော function တွေလည်းရှိပါသေးသည်။ expand_dims function သည် array တစ်ခုထဲသို့ 
#မိမိတို့ add ချင်သည့် dimension များ ထပ်မံအပ်နိုင်သည်။ expand_dims သည် parameters နှစ်ခုယူသည်။
#ပထမတစ်ခုသည် array ဖြစ်ပြီး ဒုတိယတစ်ခုသည် dimension ဖြစ်သည်။ 
#data[:,np.newaxis] သည် np.expand_dims(data,axis = 1) နှင့်တူသည်။ 
#ယခင်သင်ခန်းစာမှ col vector နှင့် တူညီသည်။

#Vstack , hstack
#array data series များကိုကိုင်တွယ်ရာတွင် တစ်ခါတစ်ရံ array များကိုပေါင်းပြီး 
##ပိုကြီးမားသည့် higher-dimensional array များ ဖန်တီးရန်လည်းလိုအပ်သေးသည်။
#ထို့ကြောင့် numpy သည် vstack နှင့် hstack functions နှစ်ခုကိုဖန်တီးထားပါသေးသည်။
#vstack function သည် parameter အနေအဖြစ်ထည့်ပေးလိုက်သော array များကို
#vertical or row အတိုင်းပေါင်းပြီးထည့်ပေးလိုက်ပါသည်။ ထိုနည်းတူ hstack ကတော့
#ထည့်ပေးလိုက်သော array များကို horizontal or col အတိုင်းပေါင်းပေးသည်။

import numpy as np

#expanddims vs vstack vs hstack
arr = np.arange(5)
arr

exp = np.expand_dims(arr,axis=1)
exp#col vector style
exp.shape

row_exp = np.expand_dims(arr,axis=0)
row_exp

vs = np.vstack((arr,arr,arr))
vs

hs = np.hstack((arr,arr,arr))
hs

vs.shape
hs.shape
