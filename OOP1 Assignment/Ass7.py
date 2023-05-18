class Time:

    def __init__(self):
        self.h = []
        self.m = []

    def addTime(self):
        for i in range(0,2):
            self.h.append(int(input('Enter Time for Object : ')))
            self.m.append(int(input('Enter Time for Object : ')))

        self.hh = sum(self.h)
        self.mm = sum(self.m)
        while self.mm >=60:
            self.hh = self.hh + 1
            self.mm = self.mm - 60
        return self.hh, self.mm

    def displayTime(self):
        print("Time:",self.hh,"Hr",self.mm,"Minutes")

    def displayMinute(self):
        while self.hh > 0:
            self.mm = self.mm + 60
            self.hh = self.hh - 1
        print("Minutes:",self.mm,"Minutes")








t =Time()
t.addTime()
t.displayTime()
t.displayMinute()