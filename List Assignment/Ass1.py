stop = int(input('Enter How many length list you want: '))

lst = []
for i in range(0,stop):
    lst.insert(i,int(input('Enter Value: ')))
sum = 0

for j in lst:
    sum = sum + j

avg = sum//len(lst)
print("Avg is", avg)