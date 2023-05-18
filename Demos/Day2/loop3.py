magicno=100
cnt=0

while cnt<3:
    cnt=cnt+1
    no=int(input("Enter no"))
    if no>100:
        print("Bigger no. pls enter smaller no")
    elif no<100:
        print("smaller no .pls enter bigger no")
    else:
        print("you win")
        break
else:
    print("Done with game.you lose the game")



'''
magicno=100


while True:
    no=int(input("Enter no"))
    if no>100:
        print("Bigger no. pls enter smaller no")
    elif no<100:
        print("smaller no .pls enter bigger no")
    else:
        print("you win")
        break
else:
    print("Done with game")

'''

    

    
