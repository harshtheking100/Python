class emp:
    pass

e=emp()

print(type(e))
print(id(e))

e1= emp()
print(type(e1))
print(id(e1))

#-------------------------------------------

#1
e.name="Sapna"
print(e.name)

print(e1.name)



#2
class emp:
    def __init__(self,empno,ename):
        self.no=empno
        self.nm=ename

e=emp(4, "Kartik")

print(e.no,e.nm)


class emp:
    def __init__(self,empno=0,ename='no name'):
        self.no=empno
        self.nm=ename

e=emp(4, "Kartik")
e1= emp()
print(e.no,e.nm)
print(e1.no,e1.nm)



#3

class emp:
    def __init__(self,empno=0,ename='no name'):
        self.no=empno
        self.nm=ename
        
    def setBonus(self,b):
        self.bonus = b
        
    def getBonus(self):
        return self.bonus

e=emp(4, "Kartik")
e.setBonus(5000)
e1= emp()
print(e.no,e.nm,e.bonus,e.getBonus())
print(e1.no,e1.nm,e1.bonus,e1.getBonus())



#4

class emp:
    location="Bengluru"
    def __init__(self,empno=0,ename='no name'):
        self.no=empno
        self.nm=ename
        
    def setBonus(self,b):
        self.bonus = b
        
    def getBonus(self):
        return self.bonus

e=emp(4, "Kartik")
e.setBonus(5000)
e1= emp()
print(e.no,e.nm,e.bonus,e.getBonus(),e.location)
print(e1.no,e1.nm,e1.location)
print(emp.location)
e1.location="Nasik"
print(e.no,e.nm,e.bonus,e.getBonus(),e.location)
print(e1.no,e1.nm,e1.location)
print(emp.location)

emp.location='kalkatta'
print(e.no,e.nm,e.bonus,e.getBonus(),e.location)
print(e1.no,e1.nm,e1.location)
print(emp.location)

#-------------------------------------------
#Overloading not allowed

class emp:
    location="Bengluru"
    def __init__(self,empno=0,ename='no name'):
        self.no=empno
        self.nm=ename
        
    def __init__(self,eno,ename,salary):
        print("overloaded Constructor")
        
e= emp()   
e=emp(1,'111',2345)     
        
#-------------------------------------------


class emp:
    location="Bengluru"
    def __init__(self,empno=0,ename='no name'):
        self.no=empno
        self.nm=ename
        
    def __del__(self):
        print("Destructor called")
        
e= emp()   
e1=emp(1,'111')  

del e
print(e.no)


#-------------------------------------------


class emp:
    location="Bengluru"
    def __init__(self,empno=0,ename='no name'):
        self.no=empno
        self.nm=ename
        
    def display(self):
        print(f"empno: {self.no} and name: {self.nm}")
        
e= emp()   
e1=emp(1,'Rupali')  

e.display()
e1.display()
print(e)

#-------------------------------------------


class emp:
    location="Bengluru"
    def __init__(self,empno=0,ename='no name'):
        self.no=empno
        self.nm=ename
        
    def __str__(self):
       return f"empno: {self.no} and name: {self.nm}"
        
e= emp()   
e1=emp(1,'Rupali')  

print(e)
print(e1)

#-------------------------------------
class emp:
    location="Bengluru"
    def __init__(self,empno=0,ename='no name'):
        self.no=empno
        self.nm=ename
        
    def __str__(self):
       return f"empno: {self.no} and name: {self.nm}"

    

lstemp=[]
for i in range(1,3):
    no= int(input("enter no"))
    nm= input("enter name")
    lstemp.append(emp(no,nm))

for i in lstemp:
    print(i)
    
    
for i in lstemp:
    if i.nm.startswith('s'):
        print(i)
        
#--------------------------------
class Person:
    pass


class Emp(Person):
    pass


e=Emp()
p=Person()

print(isinstance(e,Emp)) 
print(isinstance(e,Person)) 


print(issubclass(Emp, Person)) 
print(issubclass(Person,Emp)) 


print(hasattr(e, "name"))


#--------------------------------
class Person:
    def __init__(self,nm):
        self.name=nm


class Emp(Person):
    pass


e=Emp("Ovi")
p=Person("Sudha")

print(isinstance(e,Emp)) 
print(isinstance(e,Person)) 


print(issubclass(Emp, Person)) 
print(issubclass(Person,Emp)) 


print(hasattr(e, "name"))


#--------------------------------
class Person:
    def __init__(self,nm):
        self.name=nm


class Emp(Person):
    def __init__(self,no,nm):
        #Person.__init__(self, nm)
        super().__init__(nm)
        self.eno=no


e=Emp(5,"ovi")
p=Person("Sudha")

print(hasattr(e, "name"))
print(e.eno,e.name)


#--------------------------------
class Person:
    def __init__(self,nm):
        self.name=nm

    def display(self):
        print(self.name)

class Emp(Person):
    def __init__(self,no,nm):
        #Person.__init__(self, nm)
        super().__init__(nm)
        self.eno=no
        
    def display(self):
        #super().display()
        Person.display(self)
        print(self.eno)#,self.name


e=Emp(5,"ovi")
p=Person("Sudha")

print(hasattr(e, "name"))
print(e.eno,e.name)

e.display()

#---------------------------------------------

class A:
    id=10
    
class B:
    id=50
    
class c(B,A):
    """ This is my class show mro"""
    #id=100
    pass

    
print(c.__mro__)
print(c.id)

print(c.mro())

print(c.__doc__)
print(c.__name__)

#-------------------------------

class Account:
    def __init__(self):
        self.id =10
        self._name="protected"
        self.__balance=50000
 
acc=Account()        
print(acc.id)
print(acc.__balance) #error 


#--------------------------------------

class Time:

    def __init__(self,h=0,m=0):
         self.hh= h
         self.mm=m
         
    def display(self):
        print(self.hh,":",self.mm)
        
    def AddTime(self, t1,t2):
        self.hh=t1.hh+t2.hh
        self.mm =t1.mm+t2.mm
        
    def AddTime1(t1,t2): #class Method
        t= Time()
        t.hh=t1.hh+t2.hh
        t.mm =t1.mm+t2.mm  
        return t
        
        
        
t= Time(1,10)
t1=Time(2,30)  
t.display() 
t1.display()  

t3 = Time()  
t3.AddTime(t, t1) 
t3.display()

t4=Time.AddTime1(t, t1)
t4.display()
       
        


































