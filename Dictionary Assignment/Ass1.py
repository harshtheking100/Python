d={}

no = int(input('Enter Length of Dictionary: '))

for i in range(1,no+1):
    key = int(input('Enter Key: '))
    val = input('Enter Value: ')
    d[key] = val

print(d)