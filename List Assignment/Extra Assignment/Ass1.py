lst = [[1,2,3],[4,5,6],[7,8,9]]
l = []
for i in lst:
    mul = 1
    for j in i:
        mul = mul*j
    l.append(mul)

print(max(l))
