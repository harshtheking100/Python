#string = "this is very   funny    and cool. Indeed!"

def correction(string):
    l = string.split()
    s = " ".join(l)
    s1 = ""
    for j in range(0, len(s)):
        if s[j] == '.' and s[j+1].isalpha():
            s1 = s1 + '. '
        else:
            s1 = s1 + s[j]


    return s1

string = input('Enter String: ')

print(correction(string))