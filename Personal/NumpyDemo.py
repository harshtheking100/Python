import numpy as np

lst = [[[1,2,3,4,5],[6,7,8,9,0]],[[11,12,13,14,15],[16,17,18,19,20]]]
a = np.array(lst)
print(a)

print(type(a))
print(a.ndim)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.dtype)
print(a.data)

b = np.eye(5,4,k=0,dtype=int)
print(b)

c = np.arange(1,10).reshape(3,1,3)
print(c)

d = np.arange(1,10)
print(d)
d.resize(2,2)
print(d)
d = d.reshape(-1)
print(d)

d=d+2
print(d)
d = d*2
print(d)
d = d**3
print(d)


e = np.random.randint(1,30,(2,100))
print(e)