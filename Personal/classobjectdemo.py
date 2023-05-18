class emp:
    location = 'Pune'
    def __init__(self,empno=0,ename=None):
        self.no = empno
        self.nm = ename

    def __str__(self):
        return f"{self.no} and {self.nm} and {self.location}"

    def display(self):
        print(f"{self.no} and {self.nm}")

e = emp()
print(e)
e.display()
e1 = emp(101,'Harshal')
e1.display()
e1.location = 'Nashik'
print(e1)
emp.location = 'Mumbai'
e2 = emp(102,'Vedant')
print(e2)
e2.display()


#list of objects
lstemp = []
for i in range(3,7):
    no = int(input('Enter No: '))
    nm = input('Enter Name: ')

    lstemp.append(emp(no,nm))
for i in lstemp:
    print(i)



