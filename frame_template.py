import wx

app = wx.App()

frame = wx.Frame(None, -1, 'DRIVERS', style = wx.MAXIMIZE_BOX | wx.SYSTEM_MENU
                 |wx.CLOSE_BOX | wx.CAPTION | wx.RESIZE_BORDER | wx.MINIMIZE_BOX)
frame.Show()

app.MainLoop()
