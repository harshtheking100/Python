def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def power(a,b):
    return a**b

def ispositive(a):
    return a>0

def isnegative(a):
    return a<0

def isprime(a):
    flag = True
    for i in range(2,a):
        if a%i==0:
            flag = False
    return flag

def isarmstrong(a):
    flag1 = False
    no = a
    sum=0
    no1 = str(no)
    for i in no1:
        sum = sum + (int(i)**3)

    if no == sum:
        flag1 = True
    return flag1

