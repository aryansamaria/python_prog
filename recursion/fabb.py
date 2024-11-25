
def fibb(c,f,n,a=0,b=1):
    if n==0:
        return
    c+=1
    if c==f:
        print(a)
    return fibb(c,f,n-1,b,a+b)
n=9
f=n
c=0
fibb(c,n,f)