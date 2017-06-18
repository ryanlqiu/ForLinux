import wx
from math import  *


class Calculator(wx.Frame):
    def __init__(self, title):
        super(Calculator, self).__init__(None,title=title,size=(400,400))
        self.equation=''
        self.UIinit()
        self.Centre()
        self.Show()

    def UIinit(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.textprint = wx.TextCtrl(self, -1,'',style= wx.TE_LEFT )
        self.Text_CreateHandler(self.textprint)
        vbox.Add(self.textprint, proportion=1,flag=wx.EXPAND|wx.LEFT |wx.RIGHT|wx.TOP|wx.BOTTOM,border= 4)
        gsizer=wx.GridSizer(5,4,5,5)
        labels= ['CE','DEL','pi','Exit','7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']
        for label in labels:
            ButtonItem=wx.Button(self,label=label)
            self.Button_CreateHandler(ButtonItem,label)
            gsizer.Add(ButtonItem,1,wx.EXPAND)
        vbox.Add(gsizer, proportion=1, flag=wx.EXPAND)
        self.SetSizer(vbox)
    def Text_CreateHandler(self,TextHandler):
        self.Bind(wx.EVT_TEXT_ENTER, self.OnTarget, TextHandler)

    def Button_CreateHandler(self,button,label):
        Item = "DEL CE = Exit"
        if label not in Item:
            self.Bind(wx.EVT_BUTTON, self.OnGetInput,button)
        elif label == 'DEL':
            self.Bind(wx.EVT_BUTTON, self.OnDEL, button)
        elif label == 'CE':
            self.Bind(wx.EVT_BUTTON, self.OnCE, button)
        elif label == 'Exit':
            self.Bind(wx.EVT_BUTTON, self.OnExit, button)
        elif label == '=':
            self.Bind(wx.EVT_BUTTON, self.OnTarget, button)

    def OnGetInput(self, event):  # 得到 输入值
        eventbutton = event.GetEventObject()
        label = eventbutton.GetLabel()
        self.equation += label
        self.textprint.SetValue(self.equation)

    def OnTarget(self, event):  #  =
        string= self.equation
        try:
            target= eval(string)
            self.equation +='='
            self.equation += str(target)
            self.textprint.SetValue(self.equation)
        except:
            dlg = wx.MessageDialog(self,u'格式错误，请输入正确的等式！',u'请注意',wx.OK|wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def OnExit(self, event): #退出
        self.Close()

    def OnCE(self, event):  #清零
        self.textprint.Clear()
        self.equation=''

    def OnDEL(self, event): #回退
        self.equation = self.equation[:-1]
        self.textprint.SetValue(self.equation)


if __name__ == '__main__':
    app =wx.App()
    Calculator('Calculator')
    app.MainLoop()
