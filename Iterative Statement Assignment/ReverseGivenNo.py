num = int(input('Enter No: '))
rnum = 0
while num != 0:
    digit = num % 10
    rnum = rnum * 10 + digit
    num //= 10

print("Reversed Number:" + str(rnum))