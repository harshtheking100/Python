

print(eval('1+2'))

l=['har','afd','rdfd']
l2 = list(map(str.upper,l))
print(l2)
l4 = list(map(len, l))
print(l4)


cube = lambda a : a**3

l1 = [10,20,30]
l3 = list(map(cube,l1))
print(l3)


def ispos(a):
    return a>0

l5 = [1,-2,-3,5,-6,7]
l6=list(filter(ispos,l5))
print(l6)
l6=list(filter(lambda a : a>0,l5))
print(l6)


l = ['ABC','123','DEF','456']
l2 = list(map(int,filter(str.isdigit,l)))
print(l2)
