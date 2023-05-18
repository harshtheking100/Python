str = input('Enter String: ')

sum = 0
for i in range(0, len(str)):
    if str[i].isdigit():
        sum = sum + int(str[i])
print("Sum of Digits Present in String is", sum)