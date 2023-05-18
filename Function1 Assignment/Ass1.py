def info(name, age):
    return name,age


name = input('Enter Name: ')
age = int(input('Enter Age: '))

n,a = info(name,age)
print('Name: ',n, 'Age: ',a)