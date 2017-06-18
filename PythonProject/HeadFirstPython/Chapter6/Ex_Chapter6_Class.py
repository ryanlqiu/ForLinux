import os
import sys
os.chdir('C:\\Users\\QiuLin\\Desktop\\HeadFirstPython\\Chapter6\\ch6_data')
os.getcwd()
File_list=['james2.txt','julie2.txt','mikey2.txt','sarah2.txt']
File_Done=[]

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
            Data_Name = File_Name.readline()
            To_Name = Data_Name.strip().split(',')
        return (Athlete(To_Name.pop(0),To_Name.pop(0),To_Name))
##                FileData_Print(File_Name,each_one,file)

    except:
        print('The File Is Missing !')

class Athlete:
    def __init__(self,OwnName ,OwnBirthday = None,OwnGrades = []):
        #初始化函数 init 前后为两个下划线！！！
        #init the class state
        self.name = OwnName
        self.birthday = OwnBirthday
        self.grades = OwnGrades
    def top3(self):
        #调整时间数据格式
        Clean_Name=[float(Format_Handle(each_item)) for each_item in self.grades]
        #排序返回处理参数
        return (sorted(set(Clean_Name))[0:3])


##主函数开始
for each_one in File_list:
    File_Done=[Get_Coach_Data(each_one) for each_one in File_list]
    #类数组File_Done

