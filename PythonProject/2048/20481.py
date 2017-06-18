import curses
from random import randrange,choice
from collections import defaultdict
from gameboardcls import GameField

Actions = ['Up','Left','Down','Right','Restart','Exit'] #字母 与 行为对应
letter_Unicode = [ord(ch) for ch in 'WASDRQwasdrq' ]
Actions_dict = dict(zip(letter_Unicode,Actions * 2))   #将输入与行为关联

#获取用户输入
def GetUser_Char(keyboard):
    char = 'N'
    while char not in Actions_dict:
        char = keyboard.getch()
##        print('Reading char:',Actions_dict[char])
    return Actions_dict[char]

def transpose(field): #转置矩阵
    return [list(row) for row in zip(*field)]

def invert(field):  #矩阵逆转
    return [row[::-1] for row in field]

#初始化
def main(stdscr):
    State = 'Init'
    GameBoard = GameField(win=2048)   
    def Init():
        GameBoard.reset()
        print('Init Done')
        return 'Game'
    def Not_Game(state):
        #画出游戏界面
        GameBoard.draw(stdscr)
        Useraction = GetUser_Char(stdscr)
        responses = defaultdict(lambda:state)
        responses['Restart'],responses['Exit'] = 'Init','Exit'
        return responses[Useraction]
#Game状态处理
    def Game():
         #画出当前棋盘状态
        GameBoard.draw(stdscr)
        #读取用户输入得到action
        GameActions = GetUser_Char(stdscr)
        if GameActions == 'Restart':
            return 'Init'
        if GameActions == 'Exit':
            return 'Exit'
        if GameBoard.move(GameActions): # move successful
            if GameBoard.is_Win():
                return 'Win'
            if GameBoard.is_GameOver():
                return 'GameOver' 
        return 'Game'

    #定义状态机字典
    State_Actions = {'Init':Init,
                     'Game':Game,
                     'Win':lambda:Not_Game('Win'),
                     'GameOver':lambda:Not_Game('GameOver')
                      }
##                 'Exit':lambda:Not_Game('Exit')
                
    
    curses.use_default_colors()

    #状态机循环
    while State != 'Exit':
        State = State_Actions[State]()
##        print('State =',State)
##    GameBoard.draw(stdscr)
##    for o in range(2):
        
curses.wrapper(main)

          



        
