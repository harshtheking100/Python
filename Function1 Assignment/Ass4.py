def showEmployee(name, salary = 9000):
    return name, salary


name = input('Enter Name: ')
salary = int(input('Enter Salary: '))

print(showEmployee(name,salary))
print(showEmployee(name))