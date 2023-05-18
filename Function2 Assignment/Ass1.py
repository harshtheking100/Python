no1 = int(input('Enter len of list1: '))
lst1 = []
for i in range(0,no1):
    lst1.append(int(input('Enter value: ')))

no2 = int(input('Enter len of list2: '))
lst2 = []
for i in range(0,no2):
    lst2.append(int(input('Enter value: ')))

cnt = 0
for i in lst1:
    for j in lst2:
        if i == j:
            cnt = cnt + 1
else:
    if cnt > 0:
        print('True')
    else:
        print('False')