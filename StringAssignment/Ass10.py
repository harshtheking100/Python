str = input('Enter String: ')
ch = input('Enter Character: ')

if str.startswith(ch):
    print("String is starting with",ch)
else:
    print("String is not starting with", ch)