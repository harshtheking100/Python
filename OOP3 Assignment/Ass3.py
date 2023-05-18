import re

s1 = "Hello ABBC C"
print(list(re.finditer("[a-z]+[b]*",s1)))