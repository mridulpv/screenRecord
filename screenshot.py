import wx,os

app = wx.App(False)

s = wx.ScreenDC()
w, h = s.Size.Get()
b = wx.EmptyBitmap(w, h)
m = wx.MemoryDCFromDC(s)
i=0
while i<20:
   m.SelectObject(b)
   m.Blit(0, 0, w, h, s, 0, 0)
   m.SelectObject(wx.NullBitmap)
   b.SaveFile('{0:05d}.png'.format(i), wx.BITMAP_TYPE_PNG)
   i+=1
os.system('ffmpeg -f image2 -r 8 -i %05d.png -vcodec mpeg4 -y movie1.mp4')
i=0  
while i<20:
   os.remove('{0:05d}.png'.format(i))
   i += 1   
