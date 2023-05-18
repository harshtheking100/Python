import sys
lst = sys.argv
print(lst)

sum=0
for i in range(1,len(lst)):
    sum = sum+int(lst[i])
print(sum)
