s1 = int(input('Enter side1 of triangle: '))
s2 = int(input('Enter side2 of triangle: '))
s3 = int(input('Enter side3 of triangle: '))

if s1 == s2 == s3 :
    print('Triangle is EQUILATERAL TRIANGLE')
elif s1 != s2 != s3 :
    print('Triangle is SCALENE TRIANGLE')
elif s1 == s2 or s2 == s3 or s1 == s3 :
    print('Triangle is ISOSCELES TRIANGLE')
