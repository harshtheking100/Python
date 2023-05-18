'''3. Write a Python program to check if a string has at least one letter and one number.
Given a string in Python. The task is to check whether the string has at least one letter(character) and one number. Return "True" if the given string full fill above condition else return "False" (without quotes).

Examples:
Input: welcome2ourcountry34
Output: True
Input: stringwithoutnum
Output: False'''

'''s = "welcome2ourcountry34"

cnt = 0
if s.isalpha():
    cnt = cnt + 0
elif s.isalnum():
    cnt = cnt + 1


if(cnt > 0):
    print("True")
else:
    print("False")'''



str1=input("enter string:")
cnts=0
cntd=0

for i in range(len(str1)):
    if str1[i].isalpha():
        cnts+=1
    elif str1[i].isdigit():
        cntd+=1
if cnts>0 and cntd>0:
    print(True)
else:
    print(False)