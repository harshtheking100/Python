no1=int(input("Enter no1: "))
no2=int(input("Enter no2: "))
no3=int(input("Enter no3: "))

if no1> no2:
	if no1>no3:
		print(no1)
	else:
		print(no3)
elif no2>no3:
	print(no2)
else:
	print(no3)