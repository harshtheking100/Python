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
        print(f"No is: {self.no}")

e = Emp()
e.display()
e1 = Emp(101,'Harshal')
e1.display()

p = Person()

print("-----------------------")

print("ISINSTANCE")
print(isinstance(e,Emp))
print(isinstance(e,Person))
print(isinstance(p,Emp))
print(isinstance(p,Person))

print("----------------------------")

print("ISSUBCLASS")
print(issubclass(Emp,Person))
print(issubclass(Person,Emp))

print("----------------------------")

print("HASATTRIBUTE")
print(hasattr(e,"nm"))
print(hasattr(p,"nm"))
print(hasattr(e,"no"))
print(hasattr(p,"no"))