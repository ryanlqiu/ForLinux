import wx

"""app = wx.App()

,eNone: 当前窗口的父窗口parent，如果当前窗口是最顶层的话，则parent=None,如果不是顶层窗口，则它的值为所属frame的名字
-1: id值, -1的话程序会自动产生一个id
pos: 位置
size: 宽，高大小
还有风格参数style，不填默认是这样几个的组合
wx.MAXIMIZE_BOX| wx.MINIMIZE_BOX| wx.RESIZE_BORDER|wx.SYSTEM_MENU| wx.CAPTION| wx.CLOSE_BOX
你可以去掉几个看看效果，比如
style = wx.SYSTEM_MENU| wx.CAPTION| wx.CLOSE_BOX

frame = wx.Frame(None,-1,title='First Window',size=(200,150))

#居中处理
frame.Centre()

frame.Show()

app.MainLoop()
"""

class Example(wx.Frame):
    def __init__(self,title):
        super(Example,self).__init__(None,title=title,size=(300,400))
        self.Bind(wx.EVT_PAINT,self.OnPaint)
        self.Centre()
        self.Show()
    def OnPaint(self,event):
        dc = wx.PaintDC(self)
        dc.DrawLine(50,60,190,60)
        

if __name__ == "__main__":
    app = wx.App()
    Example("First Window")
    app.MainLoop()
        

