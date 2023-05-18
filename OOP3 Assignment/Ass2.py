import re

s1 = "abc def hty"
flag = False

lst = []
for i in range(0, len(s1)):
    if s1[i] == ' ':
        continue
    lst.append(list(re.findall("[a-zA-Z0-9]", s1[i])))

for i in lst:
    if i == []:
        flag = True
        break

if flag:
    print("Contain special char")
else:
    print("Don't contain special char")
