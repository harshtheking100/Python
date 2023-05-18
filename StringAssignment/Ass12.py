name = input('Enter Name: ')
age = int(input('Enter Age: '))
salary = int(input('Enter Salary: '))

#Using Default Formating
print("Name is {}, Age is {}, and Salary is {}".format(name,age,salary))

#Using Positional Formating
print("Name is {1}, Age is {2}, and Salary is {0}".format(salary,name,age))

#Using Keyword Formating
print("Name is {n}, Age is {a}, and Salary is {s}".format(n=name,s=salary,a=age))

#Using F Formating
print(f"Name is {name}, Age is {age}, and Salary is {salary}")

#Using %
print("Name is %s, Age is %d, and Salary is %d"%(name,age,salary))