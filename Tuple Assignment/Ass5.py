no = int(input('Enter No: '))

t = (1,2,5,6,3,8,5,2,1,4,2)

cnt = 0

for i in t:
    if i==no:
        cnt = cnt + 1

print(cnt)