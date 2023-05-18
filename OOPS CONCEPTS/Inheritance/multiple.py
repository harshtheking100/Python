class A:
    id = 10

class B:
    id = 20

class C(A,B):
    #id=30
    pass

class D(B,A):
    #id=40
    pass

print(C.id)
print(D.id)