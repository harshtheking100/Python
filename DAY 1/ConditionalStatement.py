no1 = int(input('Enter no1 : '))
no2 = int(input('Enter no2 : '))
no3 = int(input('Enter no3 : '))

print()
print('IF ELSE STATEMENT')
print()

if no1 > no2 :
    print(no1, 'is greater')
else :
    print(no2, 'is greater')






print('--------------------------------------------------')
print()
print('IF ELIF ELSE STATEMENT')
print()

if no1 > no2 and no1 > no3 :
    print(no1, 'is greater')
elif no2 > no1 and no2 > no3 :
    print(no2, 'is greater')
else :
    print(no3, 'is greater')
    




print('--------------------------------------------------')
print()
print('NESTED IF STATEMENT')
print()    
    
if no1 > no2 :
    if no1 > no3 :
        print(no1, 'is greater')
    else :
        print(no3, 'is greater')
elif no2 > no3 :
    print(no2, 'is greater')
else :
    print(no3, 'is greater')
    
    
    

print('--------------------------------------------------')
print()
print('SHORTHAND IF STATEMENT')
print()

if no1 > 0 : print(no1, 'is positive number')




print('--------------------------------------------------')
print()
print('SHORTHAND IF ELSE STATEMENT')
print()

print(no1, 'is EVEN') if (no1%2==0) else print(no1,'is ODD')
    