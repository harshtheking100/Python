r = float(input('Enter Annual Interest Rate: '))
t = int(input('Enter For How Many Year: '))
p = float(input('Enter Principal Balance: '))

si = p*(1 + (r*t))

print('Simple Interest Is : ', si)