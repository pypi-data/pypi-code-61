import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,point):
        return Point(self.x+point.x,self.y+point.y)
    
    def __sub__(self,point):
        return Point(self.x-point.x,self.y-point.y)
    
    def __mul__(self,point):
        return Point(self.x*point.x,self.y*point.y)
    
    def mid(self,point):
        return Point((self.x+point.x)/2.0,(self.y+point.y)/2.0)
    
    def distance(self,point):
        return math.sqrt((self.x-point.x)**2+(self.y-point.y)**2)
    
    def __repr__(self):
        return "({},{}) point".format(self.x,self.y)
    
    