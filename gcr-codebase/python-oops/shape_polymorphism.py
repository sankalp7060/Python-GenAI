import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def perimeter(self):
        return 2 * (self.l + self.w)

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return round(math.pi * self.r * self.r, 2)

    def perimeter(self):
        return round(2 * math.pi * self.r, 2)


shapes = [Rectangle(10, 5), Circle(7)]
for s in shapes:
    print(s.area())