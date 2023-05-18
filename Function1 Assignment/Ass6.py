def gene(start, stop):
    l = [x for x in range(start,stop) if x%2==0]
    return l


start = int(input('Enter starting range: '))
stop = int(input('Enter stop range: '))

print(gene(start,stop))