class Ass1:

    def __init__(self,no,power):
        self.n = no
        self.p = power

    def pow(self):
        x = self.n ** self.p
        return x


a = Ass1(2,3)
print(a.pow())