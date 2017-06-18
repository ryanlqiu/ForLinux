import pickle
import os
import wx



def main():
    Border = 5
    app=wx.App()
    win=wx.Frame(None,title = "Simple Editor")
    bkg=wx.Panel(win)

    LoadButton = wx.Button(bkg,label = "open")
    SaveButton = wx.Button(bkg,label = "save")

    filename=wx.TextCtrl(bkg)
    contents=wx.TextCtrl(bkg,style =wx.TE_MULTILINE | wx.HSCROLL)

    hbox=wx.BoxSizer(wx.HORIZONTAL)
    hbox.Add(filename,proportion=1,flag=wx.EXPAND)
    hbox.Add(LoadButton,proportion=0,flag=wx.EXPAND,border=Border)
    hbox.Add(SaveButton,proportion=0,flag=wx.EXPAND,border=Border)


    vbox=wx.BoxSizer(wx.VERTICAL)

    vbox.Add(hbox ,\
         proportion=0 ,\
         flag=wx.EXPAND | wx.ALL ,\
         border=Border)

    vbox.Add(contents ,\
         proportion=1 , \
         flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT ,\
         border=Border)  

    bkg.SetSizer(vbox)

    win.Show()
    app.MainLoop()

if __name__ == "__main__": main()
