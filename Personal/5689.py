l =[]
cnt = 0
for i in range(1,10000):
    if cnt == 20:
        break
    for j in range(i+1):
        if j ** 2 == i:
            l.append(i)
            cnt = cnt + 1
print(l)



lst = []
cnt = 0
no=2
while cnt<5:
    i=2
    while i<no:
        if no%i==0:
            break
        i=i+1
    else:
        lst.append(no)
        cnt = cnt + 1
    no=no+1
print(lst)