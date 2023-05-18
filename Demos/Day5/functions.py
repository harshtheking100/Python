

def display():
    '''This function display the content'''
    print("Welcome .....")
    '''this is also '''
    
display()

print(display.__doc__)


alias=display

alias()



def greet(name):
    print("WElcome ",name)


greet('Sarita')
name=input()
greet(name)


def add(a,b):
    print(a+b)

add(12,45)
add(1.2,4.5)
add([12,12,34,0],[4,5,3,2])
add("abc","pqr")
add((12,3,4,5),('a','b','c'))



def cal(a,b):
    return a+b,a-b,a*b,a/b,a//b,a%b,a**b


a,s,m,d,fd,mo,p=cal(10,5)
print(a,s,m,d,fd,mo,p)

a,*b=cal(10,5)
print(a,b)

l=[]
l=cal(10,3)
print(l)


#Required Argument
def swap(a,b):
    return b,a

a,b =swap(10,20)
print(a,b)


a,b =swap(10)



#Default Argument

def display(name='sarita',age=5):
    print(f"welcome {name} having age {age}")
    
display('aa',30)
display('aa')
display(99)



#Keyword Argument

display(age=99)
display(age=99,name="Rakesh")


#Variable length

def GreaterNo(a,*b):
    print(type(b))
    for i in b:
        if i> a:
            print(i)



GreaterNo(10,1,30,4,56,78,2,3,44)

GreaterNo(10,1,30,4,56,78)



GreaterNo(10)




def displaydata(**args):
    for k,v in args.items():
        print(k,v)


displaydata(marathi=33,Eng=66,Geo=90)
displaydata(History=33)

displaydata(marathi=33,Eng=66,Geo=90,Eng=96)



#-----------------------------------

a= lambda p:p+5
print(a(1))


a= lambda p,q:p**q
print(a(2,3))


a= lambda p,*q:p+sum(q)
print(a(2,3,2,1,4,6,7))
print(a(2))
print(a(2.1,3.2,2.4,1,4,6,7))


a= lambda p=5,q=2:p**q
print(a(2,3))
print(a())
print(a(10))
print(a(q=10,p=2))



def Myfun():
    print("Hi")

Myfun()
print(Myfun())








