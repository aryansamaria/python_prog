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
def uptoprime(num):
    n=2
    c=0
    while c<=num:
        if isarmstrong(n):
            c+=1
            if c==num:
                print(n)
        n+=1    
x=int(input())
uptoprime(x)