class Rectangle:

    def __init__(self, length1, width1):
        self.len = length1
        self.wid = width1

    def area(self):
        return self.len * self.wid


length = int(input('Enter length: '))
width = int(input('Enter width: '))
r = Rectangle(length, width)
print(r.area())
