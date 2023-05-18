l=[]
for i in range(1,100):
    sum = 0
    for j in range(1,i):
        if i%j==0:
            sum = sum + j
    if sum == i:
        l.append(i)

print(l)




lst = []
cnt = 0
no = 1
while cnt < 3:
    sum1 = 0
    i = 1
    while i < no:
        if no % i == 0:
            sum1 = sum1 + i
        i = i+1
    if sum1 == no:
        lst.append(no)
        cnt = cnt + 1
    no = no + 1

print(lst)