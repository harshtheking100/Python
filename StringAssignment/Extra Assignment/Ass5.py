#5. Write a Python Program that returns a list of Maximum Frequent Character in String
#string="welcometoknowit"
#max frequency char:['o']




s = "welcometoknowit"
l = list(s)

d = dict.fromkeys(l)
for i in range(0,len(s)):
    cnt = 0
    for j in range(0,len(s)):
        if s[i] == s[j]:
            cnt = cnt + 1
            d.update({s[i] : cnt})

l = []
for i in d.values():
    l.append(i)
m = max(l)

l1 = []
for i in d.keys():
    if d[i] == m:
        l1.append(i)
print(l1)
