lst = [11,17,19,23,26,29,35,41]
lst.sort()
print(lst)
if len(lst)%2==1:
    index = len(lst)//2
    print(lst[index])
elif len(lst)%2==0:
    i = len(lst)//2
    avg = (lst[i-1]+lst[i])/2
    print(avg)
