import math

class GFigure:
    def area(self):
        raise
NotImplementedError

class Rectangle(GFigure):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b

class Circle(GFigure):
    def __init__(self,r):
        self.r=r
    def area(self):
        return int((self.r**2)*math.pi)

class Rhomb(GFigure):
    def __init__(self,a,h):
        self.a=a
        self.h=h
    def area(self):
        return self.a*self.h

if __name__ == "__main__":
    rectangle = Rectangle(5,10)
    circle = Circle(10)
    rhomb = Rhomb(6,8)

print(f"Площадь прямоугольника: {rectangle.area()}")
print(f"Площадь круга: {circle.area()}")
print(f"Площадь ромба: {rhomb.area()}")
    
