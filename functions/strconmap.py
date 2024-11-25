st=''
def con(s):
    return st+s
stri='hai bye'
l=list(map(con,stri.split()))
a=''
for i in l:
    a+=i
print(a)    
    