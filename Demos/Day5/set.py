

s={1,2,3,4,5,6}
s1=set([5,6,7,8,9])

print(s)
print(type(s))

s.add(7)
print(s)

fs=frozenset([10,20,30])
print(fs)
fs.add(50)



print(s)
print(s1)
print(s.union(s1))
print(s.intersection(s1))
print(s.difference(s1))
print(s1.difference(s))

#{1, 2, 3, 4, 5, 6, 7}
#{5, 6, 7, 8, 9}
#{1, 2, 3, 4, 5, 6, 7, 8, 9}
#{5, 6, 7}
#{1, 2, 3, 4}
#{8, 9}