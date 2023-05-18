d = {"Arham": "Blue", "Monika": "Red", "Lisa": "Yellow", "Vinod": "Purple", "Jenny": "Pink"}
print(d)

cnt = 0

for i in d:
    cnt = cnt + 1
else:
    print("No of Students are", cnt)

d.update({"Lisa": "Orange"})
print(d)

del d["Jenny"]
print(d)

k1 = list(d.keys())
k1.sort()

for i in k1:
    print(i, d[i])
