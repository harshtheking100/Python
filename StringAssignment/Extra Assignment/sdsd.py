s = "wweelllcccooo"

l = list(s)
d = dict.fromkeys(l)

for i in range(0, len(s)):
    cnt = 0
    for j in range(0, len(s)):
        if s[i]==s[j]:
            cnt = cnt + 1
            d.update({s[i] : cnt})

l1 = []
for i in d.values():
    l1.append(i)
m = min(l1)

l2 = []
for i in d.keys():
    if d[i] == m:
       l2.append((i,d[i]))

print(l2)