import math
class Circle:
    def __init__(self,radius=1):
        self.r = radius
        print('A circle of radius:{}'.format(self.r))
    def area(self):    
        return math.pi * self.r**2
    def volume(self):
        return 4 * math.pi * self.r**3/3