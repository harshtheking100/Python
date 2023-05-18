class Ass3:

    def __init__(self):
        self.s = None

    def getstring(self):
        self.s = input('Enter String: ')

    def printstring(self):
        str1 = self.s.upper()
        print(str1)


a = Ass3()
a.getstring()
a.printstring()

