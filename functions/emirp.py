def isPrime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def reverse(n):
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        summ=summ*10+rem
        dummy//=10
    return summ
def isemirp(num):
    sum=reverse(num)
    if isPrime(num) and isPrime(sum) and sum!=num:
        return True
    else:
        return False            
def emirpNumbers(ll,ul):
    for a in range(ll,ul+1):
        if isemirp(a):
            print(a)
emirpNumbers(10,50)
