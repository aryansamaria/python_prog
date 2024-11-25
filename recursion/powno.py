def sqrt(n,p):
    if p==0:
        return 1
    elif p < 0:
        return 1 / sqrt(n, -p)
    return n*sqrt(n,p-1)
print(sqrt(2,-3))