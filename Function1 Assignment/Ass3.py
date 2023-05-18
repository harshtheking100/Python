def calculation(a,b):
    return a+b, a-b

a = int(input('Enter Value for a: '))
b = int(input('Enter Value for b: '))

add,sub = calculation(a,b)

print("Addition:", add, "Subtraction: ", sub)