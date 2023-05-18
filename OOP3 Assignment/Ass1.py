class BankAccount:

    def __init__(self, name='NA', bankaccountno=0, mobno=0, balance=0.0):

        self.name = name
        self.bankaccountno = bankaccountno
        self.__mobno = mobno
        self.__balance = balance

    def getMobNo(self):
        #mn =
        return self.__mobno

    def getBalance(self):
        #bal =
        return self.__balance

    def display(self):
        print(self.name)
        print(self.bankaccountno)
        print(self.__mobno)
        print(self.__balance)


b = BankAccount('Harshal', 1323, 9890993459, 100000)

print(b.name)
print(b.bankaccountno)

