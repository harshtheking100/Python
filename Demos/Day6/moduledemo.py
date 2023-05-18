'''
import mymath

print(mymath.ispositive(2))
print(mymath.lst)

'''
#-------------------------

import mymath as mm

print(mm.ispositive(2))
print(mm.lst)


#-------------------------

from mymath import ispositive,isodd

print(isodd(5))
print(ispositive(-2))
print(isnegative(12)) ## give error as not imported

