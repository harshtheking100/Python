no = int(input('Enter No: '))
ono = no
n = int(input('How Many Terms: '))
sum=0
for i in range(n):
    sum = sum + no
    no = (no*10)+ono

print(sum)

