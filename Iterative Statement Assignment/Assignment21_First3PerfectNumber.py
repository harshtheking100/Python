cnt = 0
no = 1
while cnt < 3:
    sum = 0

    i = 1
    while (i < no) :
        if no % i == 0:
            sum = sum + i
        i = i+1
    else:
        if sum == no:
            print(sum)
            cnt = cnt + 1
    no = no + 1



