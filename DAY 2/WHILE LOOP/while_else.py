magicno = 10
cnt = 0
while cnt < 3 :
    no = int(input('Enter No: '))
    cnt = cnt + 1
    if no < 10 :
        print('SMALLER')
    elif no > 10 :
        print('BIGGER')
    else :
        print('YOU WON')
        break
else :
    print('YOU LOSE')
