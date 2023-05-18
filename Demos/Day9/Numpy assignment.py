# -*- coding: utf-8 -*-
"""
Created on Tue May  2 16:42:43 2023

@author: Akshay
"""

#1. Create one 1-D, 2-D and 3-D array and check following attributes for all the arrays
'''
1. ndim
2. shape
3. dtype
4. size'''
#pip install numpy
import numpy as np
l=[[[1,2,3,4,5],[10,20,30,40,50]],[[6,7,8,9,10],[11,12,13,14,15]]]
l2=[1,2,3,4,5]
l3=[1,2,3,4,5],[10,20,30,40,50]

a=np.array(l,dtype=int)
b=np.array(l2,dtype=int)
c=np.array(l3,dtype=int)
print(a)
print(b)
print(c)

print(type(a))
print(a.ndim)
print(a.shape)
print(a.dtype)
print(a.size)

print("forb")
print(type(b))
print(b.ndim)
print(b.shape)
print(b.dtype)
print(b.size)

print("forc")
print(type(c))
print(c.ndim)
print(c.shape)
print(c.dtype)
print(c.size)


#2. Create 3*5 array using following types
#1. empty and a full NumPy array
#2. filled with all zeros
import numpy as np
a=np.empty((3,5),dtype=int)
print(a)

b=np.zeros((3,5),dtype=int)
print(b)

#3. filled with all ones
c=np.ones((3,5),dtype=int)
print(c)


#3. Write a NumPy program to create an array with values ranging from 14 to 40.
a=np.arange(14,41,2)
print(a)


#4. Write a progem to generate array to store 40 values in 8*5 matrix. 
a=np.random.randint(1,40,(8,5))
print(a)

#5. Write a progem to change the dimention  of above matrix to 4*10
a.resize(4,10)
print(a)

#6. Write a progem to display following things (use above matrix)
#1. display 1st 3 rows and 4 columns
a=np.random.randint(1,40,(8,5))
print(a)

for i in range(0,3):
    for j in range(0,4):
        print(a[i][j],end=" ")
    print()
#orrrr

a[0:3,0:4]

#2. display 5th column of 1st 3 rows
for i in range(3):
    print(a[i][4]) 
print(a)
#orr

a[:3,4]

#3. display only 3rd and 4th row

a[2:4]

#4. display only 3rd, 4th and 5th column
a[:,2:5]

#7. Write a program to Extract all odd numbers from above array.
a[a%2==1]


#8. Write a progem to replace all even numbers in arr with -1.(use above array)
a[a%2==0]=-1
print(a)



#9. Write a NumPy program to append values to the end of an array. (create two 1-d arrays, append
# value of 2nd array to 1st array)
a=np.arange(1,8)
b=np.arange(11,18)
print(a)
print(b)

np.append(a,b)

#10. Write a program to Convert a 1D array (Create array of 16 elements) to a 2D array with 2 rows
a=np.arange(1,17)
print(a)

a.resize(2,8)
print(a)

#11. Write a program to create array of 12 elements between 13 to 40(random), Sort the array in 
#ascending and descending
c=np.random.randint(13,40,(3,4))
print(c)
np.sort(c)

b=c.flatten()
c=np.sort(b)
c=c.reshape(3,4)
print(c)

c[::-1,::-1]


#12. Write a program to create 2-D array of 5 rows and 3 columns and do following operations
#1. Add 4 in each elements
l=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
a=np.array(l,dtype=int)
print(a)

print(a+4)

#2. multiply by 2 to each elements
print(a*2)

#3. Subtract 3 from each elements
print(a-3)

#4. Divide each element by 2
print(a/2)

#13. Write a program to create two 2-D array of 3 rows and 3 columns and perform following operations
l=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[11,22,33],[44,55,66],[77,88,99]]
a=np.array(l,dtype=int)
b=np.array(l2,dtype=int)
print(a)
print(b)

#1. Addition of two matrix
print(a+b)

#2. Subtraction of two matrix
print(a-b)

#3. Multiplication of two matrix
print(a*b)

#4. Matrix Multiplication of two matrix
print(a.dot(b))
print(a.T)

#5. Division of two matrix.
print(a/b)

#6. Find min, max, sum of resultant array elements.
print(a.min())
print(a.max())
print(a.sum())

print(a.min(axis=1))
print(a.min(axis=0))
print(a.max(axis=1))
print(a.max(axis=0))
print(a.sum(axis=1))
print(a.sum(axis=0))

