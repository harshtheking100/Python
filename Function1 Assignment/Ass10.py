no = int(input('Enter len of list: '))
lst1 = []
for i in range(0,no):
    lst1.append(int(input('Enter value: ')))

l = list(map(lambda a : a*a, lst1))
print(l)