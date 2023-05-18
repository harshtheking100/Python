stop = int(input('Enter How many length list you want: '))

lst = []
for i in range(0,stop):
    lst.insert(i,int(input('Enter Value: ')))

sumofnegative = 0
sumofEven = 0
sumofOdd = 0

for i in range(0,len(lst)):
    if lst[i] > 0:
        if lst[i]%2==0:
            sumofEven += lst[i]
        elif lst[i]%2==1:
            sumofOdd += lst[i]
    elif lst[i] < 0:
        sumofnegative += lst[i]

print("Sum of Negative Numbers is", sumofnegative)
print("Sum of Odd Numbers is", sumofOdd)
print("Sum of Even Numbers is", sumofEven)