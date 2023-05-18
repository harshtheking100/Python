l = []
while 1:
    print("1: add at last",
          "2: add by index",
          "3: delete data by value",
          "4: delete data by position",
          "5: sort data ascending order",
          "6: sort data descending order",
          "7: reverse data",
          "8: display list",
          "0: break", sep='\n')
    i = int(input("enter choice :"))

    match i:

        case 1:
            l.append(input("enter input :"))
        case 2:
            pos = int(input("enter position :"))
            value = input("enter value :")
            l.insert(pos, value)
        case 3:
            l.remove(input("value to be removed :"))
        case 4:
            l.pop(int(input("pos of value to be removed :")))
        case 5:
            l.sort()
        case 6:
            l.sort(reverse=True)
        case 7:
            l.reverse()
        case 8:
            print(l)
        case 0:
            break
