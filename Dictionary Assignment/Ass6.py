d = {"name":"Ramu","age":25,"state":"Goa"}

print(d)

l1= d["state"]
del d["state"]

d.update({"location":l1})
print(d)