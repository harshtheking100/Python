d = {"Harsh":20, "Beria":20, "varun":19, "kakunami":19, "vikas":21}

l = d.values()
l1 = list(l)
l1.sort()
l1.reverse()
print(l1)
l2 = list(set(l1))
l2.sort()
mark = l2[-2]
l3 = []
for i in d.keys():
    if d[i] == mark:
        l3.append(i)

l3.sort()
for i in range(0,len(l3)):
    print(l3[i])
