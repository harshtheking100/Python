import matplotlib.pyplot as mp

lst = ['s1', 's2', 's3', 's4', 's5']
lst1 = [45, 38, 56, 77, 80]

# mp.plot(lst, lst1)
# mp.bar(lst, lst1)  # Vertical Bar
# mp.barh(lst, lst1)  # Horizontal Bar
# mp.barh(lst, lst1, color="black")  # using color
# mp.scatter(lst, lst1)  # Scatter plot

# Using linestyle : = dotted, -- = dashed, - = solid, -. = dashdot
#mp.plot(lst, lst1, ls = ':' )

# Using markers : *, o, ., s=square, D=diamond, p=pentagon, H/h=Hexagon and many others
#mp.plot(lst, lst1, marker = 'H')

mp.plot(lst, lst1, marker = 'p', ls = '-.', color = "red" )
mp.title('Student Data')
mp.xlabel('Student Names')
mp.ylabel('Marks')
mp.show()
