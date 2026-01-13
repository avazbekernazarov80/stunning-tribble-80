# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# def a(komp, vodel, chiqdi):
#     av={'komp':komp,
#        'vodel':vodel,
#        'chiqdi':chiqdi}
#     return a
# print(a)

import wx
class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,134 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.EXPAND, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button1 = wx.Button( self, wx.ID_ANY, _(u"Да"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button1, 0, wx.ALL, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, _(u"Нет"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        bSizer1.Add( bSizer2, 1, wx.ALIGN_CENTER, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.onYes )
        self.m_button2.Bind( wx.EVT_BUTTON, self.OnCancel )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onYes( self, event ):
        event.Skip()

    def OnCancel( self, event ):
        event.Skip()
app = wx.App()
freme=MyFrame1 ( wx.Frame )
freme.Show()
app.MainLoop

