num = int(input('Enter No: '))
sum = 0
while num != 0:
    digit = num % 10
    sum = sum + digit
    num //= 10

print("Sum is:" + str(sum))