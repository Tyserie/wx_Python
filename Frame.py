import wx

class windowClass(wx.Frame):
    def __init__(self, parent, title):
        super(windowClass, self).__init__(parent, title=title,
            size =(500,300))

        self.Center()
        #self.Move(800, 400)
        self.Show()
app = wx.App()
windowClass(None, title='LANNUTTI Czech - Trucker')
app.MainLoop()
