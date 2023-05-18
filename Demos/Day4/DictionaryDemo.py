d={}
print(type(d))

d={1:10,2:20,3:{'a':0,1:30,'q':89}}
print(d)
print(d[2])
print(d[3])
print(d[3][1])


d={(1,2):10,(2,3):50}
print(d)

d=dict([(1,10),(2,20),(3,30)])
print(d)

d1={}
d1['name']="Rupesh"
d1["age"]=29
print(d1)

d1["age"]=39
print(d1)


d1.update({3:30})
print(d1)

d1.update({3:60})
print(d1)

#d1={'name': 'Rupesh', 'age': 39, 3: 60}

d={1:10,2:20,3:{'a':0,1:30,'q':89}}
d1.update(d)
print(d1)

del d1[1]
print(d1)

del d1
print(d1)

----------------------------------------
d={1: 10, 2: 20, 3: 30}
d.pop(2)
print(d)

d.pop(2) #error
print(d)

val= d.popitem()
print(d)
print(val)

d={1: 10, 2: 20, 3: 30}
k=d.pop(2)
print(d)
print(k)

#---------------------------------------------
d={}

for i in range(1,4):
    key=input("enter key")
    val=input("enter val")
    d[key]=val # d.update({key:val})
    
print(d)

#---------------------------------------------------

for k in d:
    print(k)
#---------------------------------------------------

 for k in d:
     print(d[k])
#---------------------------------------------------

for k in d.keys():
    print(k)

#---------------------------------------------------

for k in d.keys():
    print(k,d[k])
#---------------------------------------------------

for k in d.values():
    print(k)

#---------------------------------------------------

for k in d.items():
    print(k)

#---------------------------------------------------

for k,v in d.items():
    print(k,v)


---------------------------------------------
print(d)
d1=d
print(d1==d)

print('1' in d)
print(1 in d)

--------------------------------------------
print(len(d))
print(min(d))
print(max(d))
---------------------------------------------

'clear',
'copy',
'fromkeys',
'get',
'items',
'keys',
'pop',
'popitem',
'setdefault',
'update',
'values'

d.clear()
print(d)

d={1: 10, 2: 20, 3: 30}
d1=d.copy()
print(d1)

d2={}
l=[10,20,30]
d2= dict.fromkeys(l)
print(d2)

d2={}
l=[10,20,30]
d2= dict.fromkeys(l,30)
print(d2)


print(d2[40])

print(d2.get(40))
print(d2.get(20))


print(d2.get(40,100))


print(d)

p=d.setdefault(4,40)
print(p)
print(d)

p=d.setdefault(4,140)
print(p)
print(d)


#-------------------------------------
l1=[10,20,30]
l2=['a','b','c','d']

d=dict(zip(l1,l2,strict=True)) #strict=False
print(d)

d={1:20,3:40}
d1={30:60,4:89}

d3={**d,**d1}
print(d3)

#-----------------------------------------


d1={x:x**2 for x in range(1,21)}
print(d1)


li=["hi","pune","Nasik","Satara","SambhajiNagar"]
d2={x:len(x) for x in li}
print(d2)

-------------------------------------------
print(d2)
lst=sorted(d2)
print(lst)
for i in lst:
    print(i,d2[i])


print(list(reversed(d2)))