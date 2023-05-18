tu = (("harshal",50),("akshay",90))
prn = (1,2)

d = dict(zip(prn,tu))
print(d)

for i in d.values():
    if i[1]>75:
        print(i[0])

for j in d.keys():
    print(j)


for k,v in d.items():
    print(k,v)

del d[1]
print(d)
print(d[2])