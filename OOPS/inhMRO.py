class A:
    x=100
    def __init__(self,b):
        self.b=b
class B(A):
    c=200
    def __init__(self,d,e):
        self.d=d
        self.e=e  
              

print(B.__dict__)        
bo=B(2,3)
print(bo.__dict__)
print(B.mro())