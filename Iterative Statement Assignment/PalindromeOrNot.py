num = int(input('Enter No: '))
onum = num
pnum = 0
while num != 0:
    digit = num % 10
    pnum = pnum * 10 + digit
    num //= 10

if onum==pnum:
    print('Palindrome')
else :
    print('Not Palindrome')
