string = "cool.indeed"
l = string.split()
cnt = 0
for i in l:
    for j in range(0, len(i)):
        if i[j] == '.' and i[j+1].isalpha():
            cnt = cnt + 1


print(l)
print(cnt)