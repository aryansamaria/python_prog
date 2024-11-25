def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def ispalindrome(n):
    dummy=n
    sum=0
    while dummy>0:
        rem=dummy%10
        sum=sum*10+rem
        dummy//=10
    if sum==n:
        return True
    else:
        return False
def ispaliprime(num):
    if isPrime(num) and ispalindrome(num):
        return True
    else:
        return False            
def paliPrimeNumbers(ll,ul):
    for a in range(ll,ul+1):
        if ispaliprime(a):
            print(a)
paliPrimeNumbers(10,200)
