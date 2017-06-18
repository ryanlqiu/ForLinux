def change(y):
    x=globals()['x']+1
    print('x=',x)

def ChangeList(statepast):
    statepast=statepast+(5,)
    print(statepast+(5,))

x=1
state=()
##change(0)
ChangeList(state)
