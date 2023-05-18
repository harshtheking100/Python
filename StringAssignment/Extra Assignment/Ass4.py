#4. Write a Python Program that returns a list of Least Frequent Character in String.
#string="welcometoknowit"
#least frequency char:['l','c','m', 'k', 'n', 'i']


s = "wweelllcccooo"
l = list(s)
print(l)
d = dict.fromkeys(l)
for i in range(0,len(s)):
    cnt = 0
    for j in range(0,len(s)):
        if s[i] == s[j]:
            cnt = cnt + 1
            d.update({s[i] : cnt})
'''l = []
for i in d.values():
    l.append(i)
m = min(l)'''

l1 = []
for i in d.keys():
    if d[i] == min(d.values()):
        l1.append(i)


print(l1)

