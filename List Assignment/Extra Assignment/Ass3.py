lst1 = [-1, 1, -1, 8]
l1 = []
for i in range(len(lst1)):
    for j in range(len(lst1)):
        if i==j:
            continue
        if lst1[i] == lst1[j]:
            if lst1[i] not in l1:
                l1.append(lst1[i])

print(l1)


lst2 = [10,20,30,20,20,30,40,50,-20,60,60,-20,-20]
l2 = []
for i in range(len(lst2)):
    for j in range(len(lst2)):
        if i==j:
            continue
        if lst2[i] == lst2[j]:
            if lst2[i] not in l2:
                l2.append(lst2[i])

print(l2)

a="apoweirjsdfklnuioergkasdierio"
count=0
for i in a:
    if i in "aeiou":
        count=count+1

d={}
d.update({"name":"Ganesh"})
d["Id"]=123
print(d)

a=[1,2,3,4,5,6]
b=[7,8,9]
#a.append(b)
c=a+b
print(c)

str="Hello World"
vcount=lambda str:len([x for x in str if x in "aeiou"])
print(vcount(str))