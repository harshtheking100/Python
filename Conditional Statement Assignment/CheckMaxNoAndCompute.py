no1 = input('Enter no1 : ')
no2 = input('Enter no2 : ')
no3 = input('Enter no3 : ')


if int(no1) > int(no2) and int(no1) > int(no3) :
    print(no1, 'is greater')
    print(int(no1)+int(no1+no1)+int(no1+no1+no1))
elif int(no2) > int(no1) and int(no2) > int(no3) :
    print(no2, 'is greater')
    print(int(no2)+int(no2+no2)+int(no2+no2+no2))
else :
    print(no3, 'is greater')
    print(int(no3)+int(no3+no3)+int(no3+no3+no3))