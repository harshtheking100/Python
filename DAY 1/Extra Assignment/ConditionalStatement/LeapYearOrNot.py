year = int(input('Enter Year: '))

print(year,'is leap year') if year%400==0 or year%4==0 else print(year,'is not leap year')