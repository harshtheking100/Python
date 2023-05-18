num = (1,2,3,4)
num1 = (5,6,7,8)

#Display Num & Num1 tuples
print(num)
print(num1)

#Create tuple combo of num and num1
combo = num1 + num
print(combo)

#Create tuple combo2 which is sorted
combo2 = sorted(combo)
print(combo2)

#Print 3rd element of combo2
print(combo2[2])

#print last 3 elements of combo2 without using length
print(combo2[-3:])

#print length of combo2
print(len(combo2))