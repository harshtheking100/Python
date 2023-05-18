str = input('Enter String: ')

str1 = ""

for i in range(0,len(str)):
    if i%2==1:
        continue
    str1 = str1 + str[i]
else:
    print(str1)