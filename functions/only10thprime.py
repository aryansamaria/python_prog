def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def uptoprime(num):
    n=2
    c=0
    while c<=num:
        if isPrime(n):
            c+=1
            if c==num:
                print(n)
        n+=1    
x=int(input())
uptoprime(x)




