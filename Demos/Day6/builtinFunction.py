
a=10
def display():
    global a
    a=1000
    print(a)
    
    
print(a)
display()
a=20
print(a)
display()
print(a)


l=[1,2,3,4,5]
print(sum(l))

print(eval('1+2'))

eval('print("1+2")')

eval('1+2')


#-----------------------------------
#map

l=[10,20,30]
def sqr(a):
    return a*a
    
l2=map(sqr,l)
print(l2)

l2=list(map(sqr,l))
print(l2)
#---------------------------------

l=["aaaaa","bbbb",'cccc']

l2 =list(map(len,l))
print(l2)


l=["aaaaa","bbbb",'cccc']

l2 =list(map(str.upper,l))
print(l2)


l3=[1,2,4,5,6,7,8]

l4=list(map(lambda a:a*10,l3))
l4


l3=[1,2,4,5,6,7,8]
l5=[10,20,40,50,60,70,80]

l4=list(map(lambda a,b:a+b,l3,l5))
l4


a,b,c = input().split()
print(a,b,c)
print(type(a)) #str

a,b,c = map(int,input().split())
print(a,b,c)
print(type(a))

#---------------------------------

def isPositive(a):
    return a>0

l3=[-1,2,4,-5,6,-7,8]

l1=list(filter(isPositive,l3))
print(l1)


l=["aaaaa","bbbb",'ccc','a','bb','ooooo']

l2=list(filter(lambda a:len(a)>3,l))
print(l2)


l=["aaaaa","bbbb",'c%c','a','b@b','ooo12o']

l2=list(filter(lambda a:len(a)>3,l))
print(l2)




l=["aaaaa","bbbb",'c%c','a','b@b','ooo12o']

l2=list(filter(str.isalpha,l))
print(l2)

#----------------------------------------

likes,sub,views=map(int,input("Enter l , s and v").split())

if all([likes>100,sub>300,views>1000]):
    print("Excellent")
elif any([likes>100,sub>300,views>1000]):
    print("In progress")
else:
    print("Not recomanded")
