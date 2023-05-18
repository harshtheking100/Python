lst1 = [[1,2],[3,4],[5,6]]
lst2 = [[3,4],[5,7],[1,2]]

l1 = []
for i in lst1:
    if i not in lst2:
        l1.append(i)
for i in lst2:
    if i not in lst1:
        l1.append(i)

print(l1)