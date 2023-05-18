def insertion(lst):

    ele = int(input("Enter element to be insert in list: "))
    index = int(input("Enter index at which element to be inserted: "))
    lst.insert(index, ele)
    return lst



lst = [1,3,5,7,9,11]
print("List is\n",lst)
finall = insertion(lst)
print(finall)