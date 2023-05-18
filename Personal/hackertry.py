s = 'qA2'
l = s.split()
flag = False
for i in l:
    if i.isalnum():
        flag = True
print(flag)

flag = False
print(flag)
for i in l:
    if i.isalpha():
        flag = True
print(flag)

flag = False
for i in l:
    if i.isdigit():
        flag = True
print(flag)

flag = False
for i in l:
    if i.islower():
        flag = True
print(flag)

flag = False
for i in l:
    if i.isupper():
        flag = True
print(flag)
