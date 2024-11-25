def isarmstrong(n):
    dum=n
    sum=0
    l=len(str(n))
    while dum>0:
        rem=dum%10
        sum+=rem**l
        dum//=10
    if sum==n:
        return True
    else:
        return False
def armstrongnum(ll,ul):
    for i in range(ll,ul+1):
        if isarmstrong(i):
            print(i)
armstrongnum(150,155)                    