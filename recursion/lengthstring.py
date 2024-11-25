"""def le(s,c,a=0,b=1):
    if not s[a:b]:
        return c
    c+=1
    return le(s,c,b,b+1)
s='aryan'
c=0
print(le(s,c))"""
def le(s):
    if not s:
        return 0
    return 1+ le(s[1:])
s="aryan"
print(le(s))
