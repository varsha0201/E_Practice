class Rectangle():
    def __init__(self, lenght, breadth):
        self.lenght = lenght
        self.breadth = breadth

    def getArea(self):
        print(self.lenght*self.breadth," is area of reactangle.")


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        Rectangle. __init__(self,side,side)

    def getArea(self):
        print(self.side*self.side,"is area of square")

s = Square(4)
r = Rectangle(2,4)
s.getArea()
r.getArea()