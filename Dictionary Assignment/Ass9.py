d = {"Madhura Kale":"9685968911", "Ram Kulkarni":"9685967485","Rama Londhe":"9682368919"}

print(d)

d.update({"Madhura Kale":"9155510245"})
print(d)

d.update({"Ankita Deshpande":"+9855532375"})
print(d)

print(d["Ram Kulkarni"])

print(d.get("Ram Kulkarni"))

for i in d:
    print(i)

for i in d:
    print(d[i])

