import os
import sys
os.chdir('C:\\Users\\QiuLin\\Desktop\\HeadFirstPython\\Chapter6\\ch6_data')
os.getcwd()

class AthleteList(list):
    def __init__(self,Name=None,Birthday=None,Record=[]):
        list.__init__([])
        self.name = Name
        self.birthday = Birthday
        self.record = Record
    def top3(self):
        Clean_Name=[float(Format_Handle(each_item)) for each_item in self.record]
        return (sorted(set(Clean_Name))[0:3])
    
def Format_Handle(each_item):
    if '-' in each_item:
        (min,secs) = each_item.split('-',1)
    elif ':' in each_item:
        (min,secs) = each_item.split(':',1)
    else:
        return each_item
    return(min+'.'+secs)
