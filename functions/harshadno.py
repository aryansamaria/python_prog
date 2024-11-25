def isharshadnum(n):
    sum=0
    dummy=n
    while dummy>0:
        rem=dummy%10
        sum+=rem
        dummy//=10
    if n%sum==0:
        return True
    else:
        return False
def harshadnum(ll,ul):
    for i in range(ll,ul+1):
        if isharshadnum(i):
            print(i)
harshadnum(1,20)                    