#1. Write a Python program to print even length words in a string Input:
# s = "This is a python language"
#Output: This is python language


s = "This is a python language"
l = s.split()
l1 = [i for i in l if len(i)%2==0]
'''for i in l:
    if len(i)%2==0:
        l1.append(i)
'''
s2 = " ".join(l1)
print(s2)