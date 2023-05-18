def SearchByPosition(thelist):


    print("Enter what do you want to do:\n1. Find Element at position\n2. Find Element is available in list or not.")
    no = int(input('Enter Choice: '))
    try:
        if no == 1:
            pos = int(input('Enter position: '))
            if pos >= len(thelist):
                raise Exception("Position is out of list range")
            else:
                print(thelist[pos])


        if no == 2:
            ele = int(input('Enter Element: '))
            if ele in thelist:
                print(ele, 'is available in list')
            else:
                raise Exception('Element is not in list')
    except Exception as e:
        print(e)










thelist = [0,1,2,3,4,5,6,7,8,9,10]
print(thelist)
SearchByPosition(thelist)