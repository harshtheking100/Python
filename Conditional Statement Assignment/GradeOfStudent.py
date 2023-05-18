m1 = int(input('Enter marks for sub1 : ')) 
m2 = int(input('Enter marks for sub2 : ')) 
m3 = int(input('Enter marks for sub3 : ')) 
m4 = int(input('Enter marks for sub4 : ')) 
m5 = int(input('Enter marks for sub5 : ')) 

percent = (m1+m2+m3+m4+m5)/5

if percent >= 75 :
    print('Distinction')
elif 60 <= percent < 75 :
    print('First Class')
elif 45 <= percent < 60 :
    print('Second Class')
elif 35 <= percent < 45 :
    print('Third Class')
else :
    print('Fail')