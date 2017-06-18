import os
os.chdir('C:\\Users\\QiuLin\\Desktop\\HeadFirstPython\\Chapter3')
os.getcwd()
try:
    the_file=open('sketch.txt')
    for each_line in the_file:
    #if  each_line.find(':') > 0:
        try:
            (role,line_spoken)=each_line.split(":",1)
        except ValueError:
            print(each_line,end='')
        print(role,end='')
        print(' said: ',end='')
        print(line_spoken,end='')
    the_file.close()
except IOError:
    print('the data file is missing!')

        
