help(str.lower)
dir(str)

str.replace.__doc__

s="vaccine"


len(s)
Out[38]: 7

min(s)
Out[39]: 'a'

max(s)
Out[40]: 'v'

str(123)
Out[41]: '123'

#----------------------------------------

for ch in s:
    print(ch)
    
#method
s
Out[42]: 'vaccine'

s.upper()
Out[43]: 'VACCINE'

s.lower()
Out[44]: 'vaccine'


s.swapcase()
Out[46]: 'VACCINE'

s.islower()
Out[47]: True

s.isupper()
Out[48]: False

s.isspace()
Out[49]: False

s1=" "

s1.isspace()
Out[51]: True

s2='1234'

s2.isdigit()
Out[53]: True

s="i am Happy"

s.split()
Out[55]: ['i', 'am', 'Happy']

no="123-456-789"

no.split('-')
Out[57]: ['123', '456', '789']

l1=['123', '456', '789']

"#".join(l1)
Out[59]: '123#456#789'

" ".join(['i', 'am', 'Happy'])
Out[60]: 'i am Happy'

s
Out[61]: 'i am Happy'

s.index('a')
Out[62]: 2

s.rindex('a')
Out[63]: 6

s.rindex('aw')
Traceback (most recent call last):

  Cell In[64], line 1
    s.rindex('aw')

ValueError: substring not found


s.rfind('aw')
Out[65]: -1

s.find('aw')
Out[66]: -1

s.find('a')
Out[67]: 2

s.rfind('a')
Out[68]: 6



s.count('a')
Out[70]: 2
    
    
--------------------

s="thinkPoSITive"    
cap=0
low=0
for ch in s:
    if ch.islower():
        low=low+1
    elif ch.isupper():
        cap=cap+1
else:
    print(cap, low)
    
    
    
-------------------------
s="thinkPoSITive"    
v="aeiou"
con=0
for ch in s:
    if ch.isalpha():
        if ch not in v:
            con=con+1
            
else:
    print(con)
    
 ----------------------------
v="aeiou"
s= s.lower()
for ch in v:
    if s.count(ch)>0:
        print( ch ,"having freq ", s.count(ch))

 ----------------------------  
print(s) 

for i in range(0,len(s)):
    if(i %2==1):
        print(s[i].upper(),end='')
    else:
        print(s[i],end='')
 ----------------------------       
print(s)
print(s[0:3]+s[4:])
    