import os
import pickle
import nester
os.chdir('C:\\Users\\QiuLin\\Desktop\\HeadFirstPython\\Chapter3')
os.getcwd()
man=[]
otherman=[]
situation=[]
try:
    with open('sketch.txt','r') as the_file:#每一个with 语句都要有一个缩进
        with open('man.txt','w') as man_file:
            with open('otherman.txt','w') as otherman_file:
                with open('situation.txt','w') as situation_file:
                    #the_file.strip()
                    for each_line in the_file:
        #if  each_line.find(':') > 0:
                        try:
                            
                            (role,line_spoken)=each_line.split(":",1)
                            print(role,end='')
                            print(' said: ',end='')
                            print(line_spoken,end='')
                            
                            line_spoken=line_spoken.strip()
                            if role == 'Man':
                                man.append(line_spoken)
                            elif role == 'Other Man':
                                otherman.append(line_spoken)
                
                        except ValueError:
                            print(each_line,end='')
                            situation.append(each_line)
                    #pickle.dump(man,file=man_file)##pickle.dump函数 要求str 文件打开函数open 方式为'wb'/'rb'
                    nester.print_lol(man,fd=man_file)
                    nester.print_lol(otherman,fd=otherman_file)
                    nester.print_lol(situation,fd=situation_file)
except IOError:
    print('The Data File Is Missing!')
##with open('man.txt','rb') as manns_file:
##     thelist=pickle.load(manns_file)
##     for num in thelist:
##         print(num)


