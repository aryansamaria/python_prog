"""
def rev(s,n,new=''):
    if n==-1:
        return new
    new+=s[n]
    n-=1
    return rev(s,n,new)
s="heyboo"
new=''
print(rev(s,len(s)-1))

"""
def rev(s):
    if s=="":
        return ""
    return s[-1]+rev(s[:-1])
s='heyyboo'
print(rev(s))
