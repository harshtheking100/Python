#7. Given a String list, extract frequency of specific characters in the whole strings list.
#Input: test_list = ["geeksforgeeks is best for geeks"],
#chr_list = ['e', 'b', 'g", "f"]
#Output:g: 3, e:7, b: 1, T: 2)

test_list = ['geeksforgeeks is best for geeks']
chr_list = ['e', 'b', 'g', 'f']

str1 = ""
for i in test_list:
    str1 = str1 + i
l = list(str1)
print(l)

d = {}

for i in chr_list:
    cnt = 0
    for j in range(0, len(l)):
        if i == l[j]:
            cnt = cnt + 1
            d.update({i: cnt})

'''l = []
for i in d.values():
    l.append(i)
m = min(l)

l1 = []
for i in d.keys():
    if d[i] == m:
        l1.append(i)'''
print(d)


