A=[]
B=[]
for i in range(0,2):
    A.insert(i,int(input('Enter Value: ')))

for i in range(0,2):
    B.insert(i,int(input('Enter Value: ')))

print(A)
print(B)

l2=[(x,y) for x in A for y in B ]
print(l2)

