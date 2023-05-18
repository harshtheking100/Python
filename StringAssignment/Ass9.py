str = input('Enter String: ')

if len(str) < 2:
    print("")
else:
    print(str[0:2]+str[-2:])