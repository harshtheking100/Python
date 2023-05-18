no = int(input('Enter len of list: '))
lst1 = []
for i in range(0,no):
    lst1.append(int(input('Enter value: ')))

l = list(map(lambda a : a+15,lst1))

print(lst1)
print(l)


l2 = list(map(lambda a,b : a*b, l,lst1))
print(l2)

