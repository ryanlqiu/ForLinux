import os
import sys
os.chdir('C:\\Users\\QiuLin\\Desktop\\HeadFirstPython\\Chapter5\\ch5_data')
os.getcwd()
File_list=['james.txt','julie.txt','mikey.txt','sarah.txt']
def Format_Handle(each_item):
    if '-' in each_item:
        (min,secs) = each_item.split('-',1)
    elif ':' in each_item:
        (min,secs) = each_item.split(':',1)
    else:
        return each_item
    return(min+'.'+secs)

def FileData_Print(Name,filename,file=sys.stdout):
    Unique_Name=[]
    Data_Name = Name.readline()
    To_Name = Data_Name.strip().split(',')
    Clean_Name=[float(Format_Handle(each_item)) for each_item in To_Name] #列表推导 用法
    for num in Clean_Name:
        if num not in Unique_Name:
            Unique_Name.append(num)
    Unique_Name=sorted(Unique_Name)
    print(filename+'的最优秀的3个成绩：',file)
    print(Unique_Name[0:3],file)
    print(filename+'完整排序数据：',file)
    print(sorted(Clean_Name),file)

def Get_Coach_Data(filename):
    try:
        for each_one in filename:
            with open(each_one) as File_Name:
                FileData_Print(File_Name,each_one)

    except:
        print('The File Is Missing !')


Get_Coach_Data(File_list)
input('Press<Enter>')
##Get_Coach_Data('julie.txt')
##Get_Coach_Data('mikey.txt')
##Get_Coach_Data('sarah.txt')

##with open('james.txt') as James:
##    FileData_Print(James)
##with open('julie.txt') as Julie:
##    FileData_Print(Julie)
##with open('mikey.txt') as Mikey:
##    FileData_Print(Mikey)
##with open('sarah.txt') as Sarah:
##    FileData_Print(Sarah)


