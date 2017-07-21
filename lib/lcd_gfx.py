import gc

def drawLine(x0,y0,x1,y1,oled,fill):
   steep= abs(y1 - y0) > abs(x1 - x0);
   if steep:
      x0, y0 = y0, x0
      x1, y1 = y1, x1
   if x0>x1:
      x0, x1 = x1, x0
      y0, y1 = y1, y0
   dx=x1-x0
   dy=abs(y1-y0)
   err=dx/2
   ystep=-1
   if y0 < y1: ystep = 1
   for xx in range(x0, x1):
      if steep:
         oled.pixel(y0,xx,fill)
      else:
         oled.pixel(xx,y0,fill)
      err-=dy
      if err<0:
         y0+=ystep
         err+=dx
   oled.show()
   gc.collect()

def drawTrie(x0,y0,x1,y1,x2,y2,oled,fill):
   drawLine(x0,y0,x1,y1,oled,fill)
   drawLine(x2,y2,x1,y1,oled,fill)
   drawLine(x2,y2,x0,y0,oled,fill)
   oled.show()

def drawFillTrie(x0,y0,x1,y1,x2,y2,oled,fill):
   if y0 > y1:
      y0, y1=y1, y0
      x0, x1=x1, x0

   if y1 > y2:
      y2, y1=y1,y2
      x2, x1=x1,x2

   if y0 > y1:
      y0, y1=y1,y0
      x0, x1=x1,x0

   if y0 == y2:
      a = x0
      b = x0
      if x1 < a:
         a = x1
      else:
         if x1 > b:
            b = x1
      if x2 < a:
         a = x2
      else:
         if x2 > b:
            b = x2
      drawLine(a, y0,b+1,y0,oled,fill)
      return

   dx01 = x1 - x0
   dy01 = y1 - y0
   dx02 = x2 - x0
   dy02 = y2 - y0
   dx12 = x2 - x1
   dy12 = y2 - y1
   sa   = 0
   sb   = 0

   if y1 == y2:
      last = y1
   else:
      last = y1-1

   y=y0

   for y in range(y0, last+1):
      a= x0 + sa / dy01
      b= x0 + sb / dy02
      sa += dx01
      sb += dx02
      if a > b:
         a,b=b,a
      drawLine(int(a), y,int(b+1),y,oled,fill)

   sa = dx12 * (y - y1)
   sb = dx02 * (y - y0)

   for y in range(last+1, y2+1):
      a   = x1 + sa / dy12
      b   = x0 + sb / dy02
      sa += dx12
      sb += dx02
      if a > b:
         a,b=b,a
      drawLine(int(a), y,int(b+1),y,oled,fill)
   oled.show()


def drawRect(x,y,w,h,oled,fill):
   drawLine(x,y,x+w,y,oled,fill)
   drawLine(x+w-1,y,x+w-1,y+h,oled,fill)
   drawLine(x+w,y+h-1,x,y+h-1,oled,fill)
   drawLine(x,y+h,x,y,oled,fill)
   oled.show()

def drawFillRect(x,y,w,h,oled,fill):
   xa=x
   xe=x+w
   ya=y
   ye=y+h
   if xa>xe:
      xa,xe = xe,xa

   if ya>ye:
      ya,ye=ye,ya

   for yy in range(ya, ye):
      for xx in range(xa,xe):
         oled.pixel(xx,yy,fill)
   oled.show()

def drawCircle(x0,y0,r,oled,fill):
   f=1-r
   ddF_x = 1
   ddF_y = -2 * r
   x = 0
   y = r
   oled.pixel(x0  , y0+r,fill)
   oled.pixel(x0  , y0-r,fill)
   oled.pixel(x0+r, y0  ,fill)
   oled.pixel(x0-r, y0  ,fill)
   while x<y:
      if f>=0:
         y-=1
         ddF_y+=2
         f+=ddF_y
      x+=1
      ddF_x+=2
      f+=ddF_x
      oled.pixel(x0+x, y0+y, fill);
      oled.pixel(x0-x, y0+y, fill);
      oled.pixel(x0+x, y0-y, fill);
      oled.pixel(x0-x, y0-y, fill);
      oled.pixel(x0+y, y0+x, fill);
      oled.pixel(x0-y, y0+x, fill);
      oled.pixel(x0+y, y0-x, fill);
      oled.pixel(x0-y, y0-x, fill);
   oled.show()

def drawfillCircle(x0,y0,r,oled,fill):
   drawLine(x0, y0-r, x0,y0-r+2*r+1,oled, fill)
   f   = 1 - r
   ddF_x = 1
   ddF_y = -2 * r
   x = 0
   y = r
   while x<y:
      if f>=0:
         y-=1
         ddF_y+=2
         f+=ddF_y
      x+=1
      ddF_x+=2
      f+=ddF_x
      drawLine(x0+x, y0-y, x0+x, y0-y+2*y+1,oled, fill);
      drawLine(x0+y, y0-x, x0+y, y0-x+2*x+1,oled, fill);
      drawLine(x0-x, y0-y, x0-x, y0-y+2*y+1,oled, fill);
      drawLine(x0-y, y0-x, x0-y, y0-x+2*x+1,oled, fill);
   oled.show()
