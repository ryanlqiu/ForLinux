"""解决八皇后问题"""
## 主要想法：对所有情况遍历，
##一、对第一行先选定初始位置

##二、遍历第二行位置，检查是否与存在的皇后冲突
"""检查冲突，和冲突后的动作 是关键步骤"""
##若冲突，返回上一行皇后，重新选择其他位置，否则继续，

## 循环至得出结果


## 1、定义状态的表示
"""SizeOfChessBoard 表示棋盘尺寸（方形） 横向x坐标0-7  纵向y坐标0-7
   ChessBoard[] 状态表示，"""
SizeOfChessBoard = 4 
Answer=[]
state=[]
Y=0
Counter = 0
Flag = 0
##ChessBoard=[0] * SizeOfChessBoard 

## 2、定义冲突函数(针对一个新皇后)
def Trouble_CheckOneX(statepast,Xstatenow):
    Ypast=len(statepast)
    print('Ypast=',Ypast)
    if Ypast == 0:  #第一层初始化
        statepast.append(Xstatenow)
        print('第',len(statepast),'个皇后位置为',len(statepast)-1,'行',statepast[len(statepast)-1],'列')
        return False
    else:   #其它层 轮寻
        for y in range(Ypast):
            if abs(statepast[y] - Xstatenow) in (0,Ypast-y):
                # x坐标相同 或者 同一对角线
                return True
        #如果当前皇后与前面所有皇后均无冲突，则记录当前皇后位置
        statepast.append(Xstatenow)
        print('第',len(statepast),'个皇后位置为',len(statepast)-1,'行',statepast[len(statepast)-1],'列')
        return False
            
    
def TroubleCheck(statepast):
    globals()['Counter']+=1
    print('当前搜寻层数',globals()['Counter'])
    for x in range(SizeOfChessBoard):
        print('x=',x)
        print('当前行数为：',globals()['Y'])
        if Trouble_CheckOneX(statepast,x) == False:
            globals()['Y']+= 1
            if globals()['Y'] >= SizeOfChessBoard:
                print('方法已找到')
                break
            else:
                TroubleCheck(statepast) #递归
    globals()['Counter'] -= 1
    globals()['Y'] -= 1
    print('第',len(statepast)+1,'个皇后位置无法找到，返回上一层继续循环')
    if len(statepast)> 0:
        del statepast[len(statepast)-1]
    print('当前搜寻层数',globals()['Counter'])
    print('当前行数为：',globals()['Y'])
    if globals()['Counter'] <= 0:
        print('无解决方法')
    return False

TroubleCheck(state)

