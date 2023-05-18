l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ll = [1,'H',2,'A',3]
print(l)
print('-------------------')
l[2]=22
print(l)
print('-------------------')
l[3:5]=33,44
print(l)
print('-------------------')
l[5:10:2]=55,66,77
print(l)
print('-------------------')
del l[5:10:2]
print(l)
print('-------------------')

l1 = l[:]
print(id(l1))
print(id(l))
print(l1 is l)
print('-------------------')
l2 = l
print(id(l2))
print(id(l))
print(l2 is l)
print('-------------------')
l3=l.copy()
print(id(l3))
print(id(l))
print(l3 is l)
print('-------------------')
l.sort()
print(l)
print('-------------------')
l.reverse()
print(l)
print('-------------------')
l.remove(44)
print(l)
print('-------------------')
l.pop()
print(l)
print('-------------------')
l4 = [i for i in l1 if i.isalpha()]
print(l4)

