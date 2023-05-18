percent = int(input('Enter Percent for Student: '))

print()

if percent > 90 :
    print('Grade is A')
elif 80 < percent <= 90 :
    print('Grade is B')
elif 60 <= percent <= 80 :
    print('Grade is C')
elif percent < 60 :
    print('Grade is D')