unit = int(input('Enter Unit: '))

if unit <= 100 :
    print('There will be no charge')
elif 100 < unit <= 200 :
    print('The Bill is', (unit-100)*5)
elif unit > 200 :
    print('The Bill is', (((unit-200)*10)+500))