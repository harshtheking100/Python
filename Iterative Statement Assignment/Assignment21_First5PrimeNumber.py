cnt = 0
no = 2
while cnt < 5:
    i = 2
    while i < no:
        if no % i == 0:
            break
        i = i + 1
    else:
        print(no)
        cnt = cnt + 1
    no = no + 1


