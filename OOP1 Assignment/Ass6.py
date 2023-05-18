class Student:

    def __init__(self,name,roll_no):
        self.n = name
        self.rn = roll_no

    def display(self):
        print(f"Name of Student: {self.n}")
        print(f"Roll No: {self.n}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

    def setAge(self,a):
        self.age = a

    def setMarks(self,m):
        self.marks = m


s = Student('Harshal',1)
s.setAge(15)
s.setMarks(50)
s.display()