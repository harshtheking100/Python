str1 = 'ABC. DEF,,, PQR...!!!'

str2=""
for i in str1:
    if i == ',':
        str2 = str2 + '.'
    elif i == '.':
        str2 = str2 + ','
    elif i == ' ':
        str2 = str2 + ' '
    else:
        str2 = str2 + i

print(str1)
print(str2)