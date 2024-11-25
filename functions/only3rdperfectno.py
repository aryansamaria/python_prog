def isperfectno(n):
    sum=0
    for num in range(1,n//2+1):
        if n%num==0:
            sum+=num
    if sum==n:
        return True
    else:
        return False
def uptoprime(num):
    n=2
    c=0
    while c<=num:
        if isperfectno(n):
            c+=1
            if c==num:
                print(n)
        n+=1    
x=int(input())
uptoprime(x)