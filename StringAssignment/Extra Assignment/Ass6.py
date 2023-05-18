#6. Write a Python Program that returns a list of Odd Frequency Characters.
#string="welcometoknowit"
#odd frequency char [ 'T', 'c', 'o', 'm', 'k', 'n', 'i']


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
for i in d.keys():
    if d[i]%2!=0:
        l.append(i)

print(l)