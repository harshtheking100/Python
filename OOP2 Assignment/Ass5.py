class shape:

    def calculateArea(self):
        pass


class Circle(shape):

    def __init__(self):
        self.radius = int(input('Enter Radius: '))
        if self.radius is None:
            self.radius = 0

    def calculateArea(self):
        area = 3.14 * (self.radius ** 2)
        print(area)


class Square(shape):

    def __init__(self):
        self.side = int(input('Enter Side: '))
        if self.side is None:
            self.side = 0

    def calculateArea(self):
        area = self.side ** 2
        print(area)


class Rectangle(shape):

    def __init__(self):
        self.length = int(input('Enter Length: '))
        self.width = int(input('Enter Length: '))
        if self.length is None:
            self.length = 0
        if self.width is None:
            self.width = 0

    def calculateArea(self):
        area = self.length * self.width
        print(area)



s = shape()
c = Circle()
sq = Square()
r = Rectangle()
c.calculateArea()
sq.calculateArea()
r.calculateArea()