lst=[]
lst1=[1,2,3,4]
lst2=["123ASD",89.90,[123,45,67,89],"Kishor"]

lst3=["Jan","March","April"]

a,b,c=12,23,45
lst4=[a,b,c]

print(lst)
print(lst1)
print(lst2)
print(lst3)

#--------------------------------  

print(lst2[2][2])
print(lst2[-1])
print(lst2[-1][-2])
print(lst2[-1][4])
print(lst2[-1][2:])
#--------------------------------  
for i in lst2:
    print(i)
    
#--------------------------------    
for i in range(len(lst2)):
    print(lst2[i])
    
#--------------------------------  

l=[]
for i in range(0,5):
    l.append(input("Enter val"))
else:
    print(l)
    

l.insert(1,"December")
print(l)

l.insert(-1,"November")
print(l)
#-------------------------------

l5=[]
for i in range(1,6):
    no= int(input("no"))
    l5.append((no,no**2))
else:
    print(l5)
#------------------------------------

l5[0]=10
print(l5)

#------------------------------------

l5[1:3]=100,400
print(l5)

#---------------------------
del l5[0]
print(l5)

#---------------------------
del l5[1:3]
print(l5)

del l5
print(l5)
#--------------------------------------------

lst2=["123ASD",89.90,[123,45,67,89],"Kishor"]
x= lst2.pop()
print(x)

y= lst2.pop(2);
print(y)


lst2.remove(89.90)
print(lst2)

lst2.clear()
print(lst2)

#--------------------------------------------

l1=[1,2,3]
l2=[10,20,30]

print(l1+l2)
print(l1*2)
print(2 in l1)
print(5 in l1)
print(l1==l2)

l3=l1
print(l1 is l3)
print(id(l1))
print(id(l3))

l4=[1,2,3]

print(l1 is l4)
print(id(l1))
print(id(l4))

l5=l1[:]  #cloning
print(l1 is l5)
print(id(l1))
print(id(l5))
print(l1,l5,sep="\n")

print(l1==l5)

#-------------------------------------
l=[1, 2, 3, 10, 20, 30,4,2,3,2,1,2]
print(len(l))
print(min(l))
print(max(l))
print(list(('a','b','c')))

#-------------------------------------
 'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort'
 
 l2=l.copy()
 print(l)
 print(l2)
 print(l is l2)
 print(l== l2)
 
 l3=l2
 print(l3)
 print(l2)
 l3[1:3]=100,200
 print(l3)
 print(l2)
 
 
 print(l)
 print(l.count(2))
 
 print(l)
 print(l.extend(l3))
 print(l)
 
 
 
 print(l.index(100))
 
 l.sort()
 print(l)
 l.reverse()
 print(l)
 

 lst2=["123ASD",89.90,[123,45,67,89],"Kishor"]
 print(lst2)
 lst2.reverse()
 print(lst2)
 

#------------------------------------
l1=[x for x in range(1,101)]
print(l1)
#------------------------------------
l1=[x for x in range(1,101) if x%2 == 1]
print(l1)

#------------------------------------
l1=[(x,x**2,x**3) for x in range(1,101)]
print(l1)


#------------------------------------
l=["Sudha","Sarita","sharad"]
l1=[x.upper() for x in l]
print(l1)


l=["Sudha","Sarita","sharad"]
l1=[x[:2] for x in l]
print(l1)

l=["Sudha",'456',"Sarita","sharad",'123']
l1=[x for x in l if x.isdigit()]
print(l1)



l=["Sudha",'456',"Sarita","sharad",'123']
l1=[x for x in l if x.isalpha()]
print(l1)


l=["red","yellow"]
l1=["car","house"]
l3=[(x,y) for x in l for y in l1]
print(l3)



