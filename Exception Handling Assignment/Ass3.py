def print_list_element(thelist,index):
    lst = len(thelist)
    try:
        if index >=lst:
            raise Exception("Index is not in list")
        else:
            print(thelist[index])
    except Exception as e:
        print(e)








thelist = [0,1,2,3,4,5,6,7,8,9,10]
print(len(thelist))
index = int(input('Enter Index: '))
print_list_element(thelist,index)