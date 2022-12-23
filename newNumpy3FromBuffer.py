import numpy as np
#buffer data ဆိုတာပုံမှန်မဟုတ်တဲ့ data တွေကိုပြောတာ
#FromBuffer function takes 4 parameters , data(bdata),data-type,count,offset(ဘယ်နေရာကနေဘယ်နှစ်ခုစထုတ်မလဲ)

bufferData = b'nationalcybercityi'
print(type(bufferData))

#nparray = np.frombuffer(bufferData,dtype = 'S1',count=-1,offset=0)
#nparray = np.frombuffer(bufferData,dtype = 'S2',count=-1,offset=0)#even mha work tal
#nparray = np.frombuffer(bufferData,dtype = 'S2',count=9,offset=0)#even mha work tal
nparray = np.frombuffer(bufferData,dtype = 'S2',count=8,offset=1)#even mha work tal
print(nparray)
print(type(nparray))
#S1 --> string of length = 1
#count -1 ka all data will come out
#offset 0 ka from 0 to all will come out
