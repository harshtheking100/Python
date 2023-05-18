class Ass2:

    def __init__(self,string):
        self.s = string

    def reverse(self):
        j1 = self.s.split()
        j2 = j1[::-1]
        j3 = " ".join(j2)
        return j3

a = Ass2("I love my india")
print(a.reverse())


