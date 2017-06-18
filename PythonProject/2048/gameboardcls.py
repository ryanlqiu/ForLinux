from random import randrange,choice
from collections import defaultdict

class GameField(object):
    def __init__(self,width=4,length=4,win=2048):
        self.width = width    #宽
        self.length = length  #长
        self.score = 0      #当前分数
        self.highscore = 0  #最高分数
        self.win_value = win #过关分数
        self.field =[[0 for i in range(width)] for j in range(length)]
        self.reset()        #棋盘重置
    def Spawn(self): #产生一个随机数字 2 或 4
        if randrange(100) > 89:
            new_element = 4
        else:
            new_element = 2
        (i,j) = choice ([(i,j)for i in range(self.width) for j in range(self.length) if self.field[i][j] == 0])
        self.field[i][j] = new_element
    def reset(self):
        print('reset is working')
        if self.score > self.highscore:
            self.highscore = self.score
        self.score =0
        self.field =[[0 for i in range(self.width)] for j in range(self.length)]
        self.Spawn()
        self.Spawn()
        
    def draw(self, screen):
        help_string1 = '(W)Up (S)Down (A)Left (D)Right'
        help_string2 = '     (R)Restart (Q)Exit'
        gameover_string = '           GAME OVER'
        win_string = '          YOU WIN!'
        def cast(string):
            screen.addstr(string + '\n')
            #绘制水平分割线
        def draw_hor_separator():
            line = '+' + ('------+' * self.width )[0:]
            separator = defaultdict(lambda: line)  #构造一个以  line 的内容 作为值的字典
            if not hasattr(draw_hor_separator, "counter"):
                draw_hor_separator.counter = 0      #这是什么用法？
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1
        def draw_row(row):
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')
        screen.clear()
        cast('SCORE: ' + str(self.score))
        if 0 != self.highscore:
            cast('HIGHSCORE: ' + str(self.highscore))
        for row in self.field:
            draw_hor_separator()
            draw_row(row)
        draw_hor_separator()
        if self.is_Win():
            cast(win_string)
        else:
            if self.is_GameOver():
                cast(gameover_string)
            else:
                cast(help_string1)
        cast(help_string2)
        
    def is_Win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)  # ???list >= int?
    
    def is_GameOver(self):
        return not any(self.move_is_possible(move) for  move in Actions)
    def move_is_possible(self, direction):
        def row_is_left_movable(row): 
            def change(i):
                if row[i] == 0 and row[i + 1] != 0: # 可以移动
                    return True
                if row[i] != 0 and row[i + 1] == row[i]: # 可以合并
                    return True
                return False
            return any(change(i) for i in range(len(row) - 1))

        check = {}
        check['Left']  = lambda field: any(row_is_left_movable(row) for row in field)
        check['Right'] = lambda field: check['Left'](invert(field))
        check['Up']    = lambda field: check['Left'](transpose(field))
        check['Down']  = lambda field: check['Right'](transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False
    def move(self,direction): #row 为行列表
        def move_row_left(row):
            def tighten(row): #把分散的非零单元 挤到一起
                new_row = [i for i in row if i!=0]
                new_row += [0 for i in range(len(row)-len(new_row))]
                return new_row

            def merge(row): #对邻近相同元素进行合并
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        pair = False
                    else:
                        if (i + 1) < len(row) and row[i] == row[i+1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row
            return tighten(merge(tighten(row)))
##            brand_newrow=tighten(row)
##            while merge(brand_newrow) != brand_newrow:
##                brand_newrow = tighten(brand_newrow)
            
        moves={}
        #除方向左以外， 其他方向不加 [ ]
        #因为 'Left' 函数为 列表推导法 要求加 [ ]  而其他方向为函数调用（invoke）, 因此不需加 [ ],否则不符合用法，报错
        moves['Left']  = lambda field:[move_row_left(row) for row in field] 
        moves['Right'] = lambda field:invert(moves['Left'](invert(field)))
        moves['Up']    = lambda field:transpose(moves['Left'](transpose(field)))  
        moves['Down']  = lambda field:transpose(moves['Right'](transpose(field)))
        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.Spawn()
                return True
            else:
                return False
