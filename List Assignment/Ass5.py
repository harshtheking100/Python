l = [1,2,1,1,2,3,5,6,4,2,5,6]

no = int(input('Enter No to check: '))
cnt = 0
for i in l:
    if i == no:
        cnt = cnt + 1

print(cnt)