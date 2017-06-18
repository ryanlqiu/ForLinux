import os
import time
import pickle

os.chdir('C:\\Users\\QiuLin\\Desktop\\HeadFirstPython\\FilesOfPerson')
os.getcwd()
Family1=['GuoLiqiu','1992-07-28','PriceWaterhouseCoopers','10000']
class FamilyList(list):
    def __init__(self,Name=None,Birtday=None,Corporation=None,Salary=None,Others=[]):
        super(FamilyList,self).__init__()
        self.name         =  Name
        self.birthday     =  Birtday
        self.corporation  =  Corporation
        self.__salary       =  Salary
        self.others       =  Others
    def __Hello(self):
        print('Hello,World')
    def Comunication(self):
        self.__Hello()

Guo_Liqiu=FamilyList('GuoLiqiu','1992-07-28','PriceWaterhouseCoopers',10000,[])
with open('GuoLiqiu.txt','wb') as Wife:
    pickle.dump(Guo_Liqiu,Wife)

