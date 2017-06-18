import os
import sys
import pickle
os.chdir('C:\\Users\\QiuLin\\Desktop\\HeadFirstPython\\Chapter6\\ch6_data')
os.getcwd()
File_list=['james2.txt','julie2.txt','mikey2.txt','sarah2.txt']
def Format_Handle(each_item):
    if '-' in each_item:
        (min,secs) = each_item.split('-',1)
    elif ':' in each_item:
        (min,secs) = each_item.split(':',1)
    else:
        return each_item
    return(min+'.'+secs)

def FileData_Print(Name,filename,file=sys.stdout):
    Name_Dict = {}
    Unique_Name=[]
    #转化为列表
    Data_Name = Name.readline()
    To_Name = Data_Name.strip().split(',')
    
    #取出选手的姓名和生日
    Name_Dict['PlayerName'] = To_Name.pop(0)
    Name_Dict['DateOfBirth'] = To_Name.pop(0)
    
    #统一数据格式
    #列表推导用法
    Clean_Name=[float(Format_Handle(each_item)) for each_item in To_Name] 
    for num in Clean_Name:
        if num not in Unique_Name:
            Unique_Name.append(num)
    Unique_Name=sorted(Unique_Name)
    Name_Dict['PlayerData'] = Unique_Name
    #输出数据
    pickle.dump(Name_Dict['PlayerName']+'的最优秀的3个成绩：',file)
    pickle.dump(Name_Dict['PlayerData'][0:3],file)
    pickle.dump(Name_Dict['PlayerName']+'的完整排序数据：',file)
    pickle.dump(sorted(Clean_Name),file)

def Get_Coach_Data(filename,file=sys.stdout):
    try:
        for each_one in filename:
            with open(each_one) as File_Name:
                FileData_Print(File_Name,each_one,file)

    except:
        print('The File Is Missing !')

with open('HandleData.txt','wb') as HandleData:
    Get_Coach_Data(File_list,file=HandleData)
