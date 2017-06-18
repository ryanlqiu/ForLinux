import os
import sys
import pickle
os.chdir('C:\\Users\\QiuLin\\Desktop\\HeadFirstPython\\Chapter6\\ch6_data')
os.getcwd()
List=[]
##不管dump几次 一直调用load函数 直到抛出异常EOFError
with open('HandleData.txt','wb') as HandleData:
    pickle.dump('PlayerName:',file=HandleData)
    pickle.dump('111PlayerName:',file=HandleData)
with open('HandleData.txt','rb') as Handle_Data:
    try:
        while 1 < 2:
            A=pickle.load(Handle_Data)
            List.append(A)
    except EOFError:
        print(List)
    
##    List1=pickle.load(Handle_Data)
##    List2=pickle.load(Handle_Data)
    
##    print(List1)
##    print(Handle_Data)
