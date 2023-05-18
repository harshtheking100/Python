def filter_long_word(lst,n):
    word = []
    for i in lst:
        if len(i) > n:
            word.append(i)
    return word


no = int(input('Enter len of list: '))
lst1 = []
for i in range(0,no):
    lst1.append(input('Enter value: '))

size = int(input('Enter size to check if list have words having length bigger than size: '))

lst2= filter_long_word(lst1,size)
print(lst2)