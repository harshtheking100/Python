l = []
cnt = 0
for i in range(1,100):
    if cnt == 10:
        break
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            l.append(i)
            cnt = cnt + 1
print(l)