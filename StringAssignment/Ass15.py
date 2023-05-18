str = input('Enter String: ')

cnt = 0

if str.isalpha():
    for i in str:
        cnt = cnt + 1
    print("Total no of Alphabets are",cnt)
else:
    for i in range(0,len(str)):
        if str[i].isalpha():
            cnt = cnt + 1
    print("Total no of Alphabets are",cnt)