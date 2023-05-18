def l1(lst1):
    l2 = list(set(lst1))
    l2.sort()
    return l2

no = int(input('Enter len of list: '))
lst1 = []
for i in range(0,no):
    lst1.append(int(input('Enter value: ')))

print(l1(lst1))
