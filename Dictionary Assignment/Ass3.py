n = int(input('Enter Value: '))

d = {x:x*x*x for x in range(1,n)}
print(d)


#another way
#d1 = {}
#for i in range(1,n):
#    key = i
#   val = i*i*i
#    d1[key] = val
#print(d1)