def func1(*len):
    l=[]
    for i in len:
        l.append(i)
    return l


no = int(input('Enter length of list: '))
lst=[]
for i in range(0,no):
    lst.insert(i,int(input('Enter value: ')))

print(func1(lst))