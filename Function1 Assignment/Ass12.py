no = int(input('Enter len of list: '))
lst1 = []
for i in range(0,no):
    lst1.append(int(input('Enter value: ')))


square = list(map(lambda a : a*a,lst1))
cube = list(map(lambda a : a*a*a,lst1))

print(lst1)
print(square)
print(cube)