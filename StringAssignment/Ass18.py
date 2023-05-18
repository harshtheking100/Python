s = input('Enter String: ')

for i in range(0,len(s)+1):
    for j in range(i):
        print(s[j],end='')
    print()