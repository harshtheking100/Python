lst1 = [[4,1,6],[7,8],[4,10,8]]
l1 = []

for i in lst1:
    sum = 0
    for j in i:
        sum = sum + j
    l1.append(sum)

print(l1)
