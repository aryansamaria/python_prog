def maX(l,c,a=0,b=1):
    if not l[a:b]:
        return c
    if l[a:b][0]>=c:
        c=l[a:b][0]
    return maX(l,c,b,b+1)
l=[2,3,5]
print(maX(l,0))