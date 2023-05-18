s = "string slicing in python"

print(s[0:2],end=' ')
for i in range(0,len(s)):
    if s[i].isspace():
        print(s[i+1:i+3],end=' ')