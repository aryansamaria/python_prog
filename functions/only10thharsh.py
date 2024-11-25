def isharshad(n):
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
def uptoprime(num):
    n=2
    c=0
    while c<=num:
        if isharshad(n):
            c+=1
            if c==num:
                print(n)
        n+=1    
x=int(input())
uptoprime(x)  