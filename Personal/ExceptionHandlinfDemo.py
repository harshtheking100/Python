#print(Exception.__subclasses__())


try:
    no1 = int(input('Enter No 1: '))
    no2 = int(input('Enter No 2: '))
    print(no1/no2)
except Exception as e:
    print(e)

