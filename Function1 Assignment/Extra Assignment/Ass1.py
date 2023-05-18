def fact(i):
    f=1
    for i in range(2,i+1):
        f = f*i
    return f


def Main():
    no = int(input('Enter start: '))
    no1 = int(input(('Enter stop: ')))
    for i in range(no,no1+1):
        print(i, fact(i))


Main()