price = int(input('Enter Cost of Bike: '))



if price > 100000 :
    tax = price * 0.15
    print('Tax to be paid is: ', tax)
elif 50000 < price <= 100000 :
    tax = price * 0.10
    print('Tax to be paid is: ', tax)
elif price >= 50000 :
    tax = price * 0.05
    print('Tax to be paid is: ', tax)