row = 5

space = row-1

for i in range(row):
    for j in range(space):
        print('',end=' ')

    space = space - 1
    for k in range(i+1):
        print('*',end=' ')
    print()