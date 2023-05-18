stop = int(input('Enter How many length list you want: '))

lst = []
for i in range(0,stop):
    lst.insert(i,int(input('Enter Value: ')))

odd = []
even = []

for i in range(0,len(lst)):
    if lst[i]%2==0:
        even.append(lst[i])
    elif lst[i]%2==1:
        odd.append(lst[i])

print(odd)
print(even)