def find_longest_word(lst):
    max = 0
    word = ""
    for i in lst:
        if len(i) > max:
            max = len(i)
            word = i
    return max, word


no = int(input('Enter len of list: '))
lst1 = []
for i in range(0,no):
    lst1.append(input('Enter value: '))

len, word = find_longest_word(lst1)

print("The longest word in list is",word)
print("The length of longest word is",len)

