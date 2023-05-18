class Dealers:

    def __init__(self,id=None,name=None,mobileno=None,address=None):
        self.id = id
        self.name = name
        self.mobileno = mobileno
        self.address = address

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Mobile: {self.mobileno}, Address: {self.address}"


lstd = []
for i in range(0,5):
    print('Enter Details for Dealer',i)
    id = int(input('Enter ID: '))
    name = input('Enter Name: ')
    mobileno = input('Enter Mobile No: ')
    address = input('Enter Address: ')
    lstd.append(Dealers(id,name,mobileno,address))

for i in lstd:
    if i.address == 'Pune' and i.mobileno == i.mobileno[::-1]:
        print(i)