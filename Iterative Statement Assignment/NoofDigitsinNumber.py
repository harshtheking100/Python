num = int(input('Enter No: '))
rnum = 0
cnt = 0
while num > 0:
    num //= 10
    cnt = cnt + 1


print("No of Digits in Number is:" + str(cnt))