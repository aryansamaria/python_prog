def count(s,e,c,a=0,b=1):
    if not s[a:b]:
        return c
    if s[a:b]==e:
        c+=1
    return count(s,e,c,b,b+1) 
s="aryyaan" 
print(count(s,'a',0)  )