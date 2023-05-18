class Person():

    def __init__(self, pid=0, pname='NA', emailid='NA', mobno=0):
        self.pid = pid
        self.pname = pname
        self.emailid = emailid
        self.mobno = mobno

    def display(self):
        print('PID:', self.pid)
        print('PNAME:', self.pname)
        print('EMAIL-ID:', self.emailid)
        print('MOBILE NO:', self.mobno)


class Employee(Person):

    def __init__(self, dept='NA', desg='NA', sal=0):
        super().__init__(230343025005, 'Harshal', 'harshalamrutkar1@gmail.com', 9890993459)
        self.dept = dept
        self.desg = desg
        self.sal = sal

    def setDept(self, dept1):
        self.dept = dept1

    def getDept(self):
        return self.dept

    def setDesg(self, desg1):
        self.desg = desg1

    def getDesg(self):
        return self.desg

    def setSal(self, sal1):
        self.sal = sal1

    def getSal(self):
        return self.sal

    def calculateNetSal(self):
        fivepercent = self.sal - (self.sal * 0.05)
        fifteenpercent = self.sal + (fivepercent * 0.15)
        tenpercent = self.sal + (fifteenpercent * 0.10)
        self.Netsal = self.sal + tenpercent
        print('NET SALARY:',self.Netsal)

    def display(self):
        super().display()
        print('DEPARTMENT:',self.dept)
        print('DESIGNATION:', self.desg)
        print('SALARY:', self.sal)


class Member(Person):

    def __init__(self, membertype='NA', amtpaid=0):
        super().__init__(230343025005, 'Harshal', 'harshalamrutkar1@gmail.com', 9890993459)
        self.membertype = membertype
        self.amtpaid = amtpaid

    def setMemberType(self, mt):
        self.membertype = mt

    def getMemberType(self):
        return self.membertype

    def setAmtPaid(self, amtp):
        self.amtpaid = amtp

    def getAmtPaid(self):
        return self.amtpaid

    def display(self):
        super().display()
        print('MEMBER TYPE:', self.membertype)
        print('AMT PAID:', self.amtpaid)




p = Person()
e = Employee()
e.setDept('CORE DEVELOPERS')
e.setDesg('JAVA DEVELOPER')
e.setSal(1200000)
m = Member()
m.setMemberType('VVIP')
m.setAmtPaid(100000)
e.display()
print('--------------------')
e.calculateNetSal()
print('--------------------')
m.display()

