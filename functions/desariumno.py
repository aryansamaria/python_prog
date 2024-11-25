def isdesarium(n):
    dum=n
    sum=0
    l=len(str(n))
    while dum>0:
        rem=dum%10
        sum+=rem**l
        l-=1
        dum//=10
    if sum==n:
        return True
    else:
        return False
def desariumno(ll,ul):
    for i in range(ll,ul+1):
        if isdesarium(i):
            print(i)
desariumno(1,100)                    