def tup(start, stop):
    l = [(x,x*x) for x in range(start,stop+1)]
    return l


start = int(input('Enter starting range: '))
stop = int(input('Enter stop range: '))

print(tup(start,stop))