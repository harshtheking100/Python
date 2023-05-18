lst = [12,67,98,34]
l1 = []
for i in lst:
    l1.append(str(i))
l2 = []
for i in l1:
    sum = 0
    for j in i:
        sum = sum + int(j)
    l2.append(sum)
print(l2)

