#flatten() function ဆိုသည်မှာ multidimensional array တွေကို flattened one-dimensional array များအဖြစ်ပြန်ပြောင်းပေးသည်။ 
#multidimensional array မှာပါသည့် element အရေအတွက်အတိုင်း flattened array ရဲ့ length ကိုပြန်ပေးသည်။ 
# ဆိုလိုချင်တာက row 2 ခု col နှစ်ခုရှိတဲ့ #array တစ်ခုမှာ element အားဖြင့်လေးခုရှိတယ်။ ထို array အား flatten လုပ်မည်ဆိုလျှင် အသစ်ရလာသော array ရဲ့ length ဟာလည်း ၄ခုရှိနေမည်ဖြစ်သည်။ 
import numpy as np
data = np.array([[1,2,3],[4,5,6]])
data.shape
#to flaten
flat = data.flatten()
flat.shape#row only

#new Axis
#one dimensional array ကနေမှတစ်ဆင့် မိမိလိုသလို row vector or column vector array များဖန်တီးလိုတဲ့အခါမှာ newaxis ဆိုသည့် function ကိုသုံးနိုင်သည်။ 
#newAxis သည်ရှိပြီးသား data များထဲသို့ နောက်ထပ် Axis တစ်ခုထပ်ထည့်ပေးမှာပါ။ ပထမဆုံးအနေအဖြစ် arange ကိုသုံးပြီး elements 5 ခုပါသည့် array တစ်ခုကိုတည်ဆောက်ပါမည်။ ထို array သည် ပုံမှန် one 
#dimension array သာဖြစ်သည်ကိုသတိပြုပါ။



#new Axis
row_vec = flat[np.newaxis,:]
row_vec
#[[]]
col_vec = flat[:,np.newaxis]
col_vec

col_vec.shape


new_arr = row_vec + col_vec
new_arr
new_arr.shape
