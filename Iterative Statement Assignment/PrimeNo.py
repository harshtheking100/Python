start = int(input("Enter Starting No: "))
stop = int(input("Enter Stop No: "))
for i in range(start,stop+1):
    for j in range(2,(i//2)+1):
        if i % j == 0:
            break
    else:
        print(i)