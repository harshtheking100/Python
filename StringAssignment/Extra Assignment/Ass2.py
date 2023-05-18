#2. Write a Python program to capitalize the first and last character of each word in a string. Given the string, the task is to capitalise the first and last character of each word in a string.

#Examples:
#Input: hello world

#Output: Hello WorlD

s = "hello world"
l = s.split()
l1 = []

for i in l:
    str1 = ""
    for j in range(0,len(i)):
        if j == 0 or j == len(i)-1:
            str1 = str1 + i[j].upper()
        else:
            str1 = str1 + i[j]
    l1.append(str1)

s2 = " ".join(l1)
print(s2)