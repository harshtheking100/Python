str = input('Enter String: ')

low = 0
up = 0

for i in str:
    if i.isupper():
        up += 1
    elif i.islower():
        low += 1

print("The No of UpperCase Characters are", up)
print("The No of LowerCase Characters are", low)
