class Student:

    def __init__(self, roll_no=0, name='NA', course='NA', marks=None):
        if marks is None:
            marks = {}
        else:
            marks = {}
        self.srn = roll_no
        self.sname = name
        self.scourse = course
        self.smarks = marks

    def __str__(self):
        return f"Roll No: {self.srn} \nStudent Name: {self.sname} \nStudent Course: {self.scourse} " \
               f"\nStudent Marks: {self.smarks}"

    def enterdata(self):
        self.srn = int(input('Enter Roll No: '))
        self.sname = input('Enter Name: ')
        self.scourse = input('Enter Course: ')
        for i in range(0, 5):
            key = input('Enter Subject Name: ')
            val = int(input('Enter Marks: '))
            self.smarks[key] = val
        self.slist = [self.srn, self.sname, self.scourse, self.smarks]

    def display(self):
        print(self.slist)



std1 = Student()
std2 = Student()
std3 = Student()
lststudentobj = [std1, std2,std3]
for i in lststudentobj:
    i.enterdata()

for i in range(0,len(lststudentobj)):
    for j in lststudentobj[i].smarks.values():
        if j < 40:
            print(lststudentobj[i])

