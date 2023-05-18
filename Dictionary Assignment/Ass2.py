d1 = {1:'H', 2:'A', 3:'R', 4:'S', 5:'H', 6: 'A', 7: 'L'}
d2 = {1: 'A', 5: 'B', 8: 'C'}
d5 = {2: 'D', 4: 'E', 6: 'F'}
d3 = {}
#d3 = d1.add(d2)
#d1.update(d2)
d3.update(d2)
d3.popitem()

d4 = dict([(1,2),(3,4)])
print(d4)

d6 = {**d2, **d5}
print(d6)