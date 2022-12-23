import numpy as np
#iterable ဖြစ်တဲ့ကောင်တွေကနေပြီးတော့ data တွေထုတ်ယူတာကို fromIter နဲ့ သုံးလို့ရတယ်
#FromIter
myDList = [1,2,3,4,5,6]
arr = np.fromiter(myDList,dtype=int) #np.fromiter(iterable,dtype)
print(arr,type(arr))

#from array incremental sequence
#arrange


arrObj = np.arange(0,20,2)#int data handle
print(arrObj)

#linspace incremental sequence non-integer
arrOj = np.linspace(0,20,3)#count 0 နဲ့ 20 ကြား ၃ လုံး
print(arrOj)
#arrOj = np.linspace(0,20,10)#count 
#print(arrOj)

arrOj = np.linspace(0,20,100)#count 
print(arrOj)
