l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

no = int(input('Enter No: '))
for i in range(0,len(l)):
    if no == l[i]:
        print(i)