import os
import sys
import pickle
os.chdir('C:\\Users\\QiuLin\\Desktop\\HeadFirstPython\\Chapter6\\ch6_data')
os.getcwd()
List=[]
File_list=['james2.txt']
def Format_Handle(each_item):
    if '-' in each_item:
        (min,secs) = each_item.split('-',1)
    elif ':' in each_item:
        (min,secs) = each_item.split(':',1)
    else:
        return each_item
    return(min+'.'+secs)

def Get_Coach_Data(filename,file=sys.stdout):
    try:
        with open(filename) as File_Name:
            FileData_Print(File_Name,filename,file)

    except:
        print('The File Is Missing !')
        
def FileData_Print(Name,filename,file=sys.stdout):
    Name_Dict = {}
    Unique_Name=[]
    #转化为列表
    Data_Name = Name.readline()
    To_Name = Data_Name.strip().split(',')
    
    #取出选手的姓名和生日
    Name_Dict['PlayerName'] = To_Name.pop(0)
    Name_Dict['DateOfBirth'] = To_Name.pop(0)
    Clean_Name=[float(Format_Handle(each_item)) for each_item in To_Name]
    Name_Dict['PlayerData'] = sorted(Clean_Name)
    #输出数据
    pickle.dump(Name_Dict['PlayerName']+'的最优秀的3个成绩：',file)
    pickle.dump(Name_Dict['PlayerData'][0:3],file)
    pickle.dump(Name_Dict['PlayerName']+'的完整排序数据：',file)
    pickle.dump(sorted(Clean_Name),file)

with open('HandleData.txt','wb') as HandleData:
    Get_Coach_Data('james2.txt',file=HandleData)

with open('HandleData.txt','rb') as Handle_Data:## 修正版的load函数
    try:
        while 1 < 2:
            A=pickle.load(Handle_Data)
            List.append(A)
    except EOFError:
        print(List)
