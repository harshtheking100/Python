str = input('Enter String: ')

vowel = "aeiouAEIOU"
cnt = 0

for i in str:
    if i in vowel:
        cnt = cnt + 1
else:
    print(cnt)

