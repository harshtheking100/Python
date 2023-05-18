try:
    while 1:
        try:
            age = int(input('Enter Age: '))
        except:
            print('Enter valid Age: ')
        else:
            break

    while 1:
        try:
            height,weight = map(float,input('Enter Height and Weight: ').split())
        except:
            print('Enter Valid Height or  Weight: ')
        else:
            break

    while 1:
        try:
            Name, Surname = map(str, input('Enter Name & Surname: ').split())
            if Name.isalpha() and Surname.isalpha():
                break
            else:
                raise Exception('Enter Valid Name or Surname: ')
        except Exception as e:
            print(e)
        else:
            break
except Exception as e:
    print(e)
else:
    print("Age:",age)
    print("Height:", height)
    print("Weight:", weight)
    print("Name:", Name)
    print("Surname:", Surname)


