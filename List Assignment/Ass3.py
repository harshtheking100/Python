stop = int(input('Enter How many length list you want: '))

lst = []
for i in range(0,stop):
    lst.insert(i,int(input('Enter Value: ')))

odd = 0
even = 0

for i in range(0,len(lst)):
    if lst[i]%2==0:
        if lst[i] > even:
            even = lst[i]
    elif lst[i]%2==1:
        if lst[i] > odd:
            odd = lst[i]

print("The Largest Odd number is", odd)
print("The Largest Even number is", even)