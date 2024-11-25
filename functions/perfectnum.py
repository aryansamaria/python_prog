def isperfectnum(n):
    sum=0
    for num in range(1,n//2+1):
        if n%num==0:
            sum+=num
    if sum==n:
        return True
    else:
        return False
def perfectnum(ll,ul):
    for i in range(ll,ul+1):
        if isperfectnum(i):
            print(i)
perfectnum(1,10)                    