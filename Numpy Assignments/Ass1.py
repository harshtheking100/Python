import numpy as np

a = np.arange(1,10)
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)
print(a.size)

print()
print('------------------------')
print()

b = np.arange(1,10)
b.resize(2,2)
print(b)
print(b.ndim)
print(b.shape)
print(b.dtype)
print(b.size)




c = np.ones((2,3,4),dtype=int)
print(c)
print(c.ndim)
print(c.shape)
print(c.dtype)
print(c.size)
