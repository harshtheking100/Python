str = input('Enter String: ')

vowel = "aeiouAEIOU"
cnt = 0
for i in str:
    if i not in vowel:
        cnt = cnt + 1
else:
    print("The No of Consonents in the String are",cnt)