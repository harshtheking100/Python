l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l1 = []
for i in l:
    if i not in l1:
        l1.append(i)

print(l1)