class Person:

    def __init__(self,name=None):
        self.nm = name

    def display(self):
        print(f"Name is: {self.nm}")


class Emp(Person):

    def __init__(self,empno=0,name=None):
        super().__init__(name)
        self.no = empno

    def display(self):
        super().display()
        print(f"Emp No is: {self.no}")


class Developer(Emp):

    def __init__(self,empno=0,name=None,designation=None):
        super().__init__(name,empno)
        self.job = designation

    def display(self):
        super().display()
        print(f"Designation is: {self.job}")


d = Developer()
d.display()
print("-----------------------")
d1 = Developer(101,'Harshal')
d1.display()
print("-----------------------")
d2 = Developer(101,'Harshal','Java Developer')
d2.display()