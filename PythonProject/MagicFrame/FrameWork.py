import wx
import math
from abc import ABCMeta,abstractmethod
__author__ = 'RyanQiu'


class Point(object):

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @property
    def xy(self):
        return (self.x, self.y)

    def __str__(self):
        return "x={0}, y={0}".format(self.x, self.y)

    def __repr__(self):
        return str(self.xy)

    @staticmethod
    def dist(a, b):
        return math.sqrt((a.x-b.x) ** 2 +(a.y-b.y) ** 2)


class Polygon(object):
    __metaclass__ = ABCMeta

    def __init__(self, pointlist, **kwargs):
        for pointer in pointlist:
            assert isinstance(pointer, Point), "Input must be Point type"
        self.points=pointlist[:]
        self.points.append(pointlist[0])   #要画完一个完整的多边形，最后要回到初始点
        self.color=kwargs.get('color', '#000000')

    def drawpoints(self):
        point_xy=[]
        for pointer in self.points:
            point_xy.append(pointer.xy)
        print(point_xy)
        return tuple(point_xy)

    @abstractmethod
    def area(self):
        raise ( "area function is not implemented" )

    def __lt__(self, other):
        return self.area < other.area

    def __ge__(self, other):
        return self.area > other.area


class RectAngle(Polygon):
    def __init__(self, startpoint, width, length, color):
        self.width= width
        self.length= length
        self.color =color
        Polygon.__init__(self, [startpoint,startpoint + Point(self.width, 0), startpoint + Point(self.width, self.length), startpoint + Point(0, self.length)],color=self.color )

    def area(self):
        return self.width * self.length

class TriAngle(Polygon):
    def __init__(self, TirPoints, color):
        self.tripoints = TirPoints[:]
        assert self.Tri_is_possible(), "Points Can't compose a TriAngle"
        Polygon.__init__(self, self.tripoints, color=color)
        self.color = color

    def area(self):
        return 1
    def Tri_is_possible(self):
        delta_X1=abs(self.tripoints[0].x - self.tripoints[1].x)
        delta_Y1=abs(self.tripoints[0].y - self.tripoints[1].y)
        delta_X2=abs(self.tripoints[0].x - self.tripoints[2].x)
        delta_Y2=abs(self.tripoints[0].y - self.tripoints[2].y)
        # print('delta_X1 =',delta_X1,'delta_X2=',delta_X2)
        # print('delta_Y1 =', delta_Y1, 'delta_Y2=', delta_Y2)
        deltaX=delta_X1/delta_X2
        deltaY=delta_Y1/delta_Y2
        # print('deltaX=',deltaX,'deltaY=',deltaY)
        if(deltaX== deltaY):
            return False
        else:
            return True

##实例化 实体
class Example(wx.Frame):

    def __init__(self, title, shapes):
        super(Example, self).__init__(None,title=title, size=(300, 400))
        self.shapes = shapes
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Centre()
        self.Show()

    def OnPaint(self, event):
        dc=wx.PaintDC(self)
        for shape in self.shapes:
            dc.SetPen(wx.Pen(shape.color))
            dc.DrawLines(shape.drawpoints())



if __name__=='__main__':
    perpar_to_draw=[]
    Tri=[Point(200,120), Point(210,160), Point(150,180)]
    start_p=Point(50,50)
    SanJiao=TriAngle(Tri, color="#ff0000")
    ChangFang=RectAngle(start_p, 100, 80, color="#fff000")
    perpar_to_draw.append(ChangFang)
    perpar_to_draw.append(SanJiao)
    app = wx.App()
    Example('DrawingPic',perpar_to_draw)
    app.MainLoop()
