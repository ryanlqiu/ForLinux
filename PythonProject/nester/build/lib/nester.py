"""Module Name:  print_lol
      Describe:  采用嵌套调用的函数形式
      Function:显示嵌套列表中的数据，每项数据占一行。"""
import sys
def print_lol(the_list,level=0,fd=sys.stdout):
#print_lol
        for each_item in the_list:
                if isinstance(each_item,list):
                        print_lol(each_item,level+1,fd)
                else:
                        for num in range(level):
                                print("\t",end='')
                        print(each_item,file=fd)
