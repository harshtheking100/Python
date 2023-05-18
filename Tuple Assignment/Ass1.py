no = int(input('Enter Length of List: '))
l1 = []
for i in range(0,no):
    l1.append(int(input('Enter Value: ')))

#Using List
l2 = [(i,i*i) for i in l1]

#Using Range Function
#lst = [(i,i*i) for i in range(1,11)]

print(l2)