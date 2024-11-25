def rev(s):
    if s=="":
        return ""
    return s[-1]+rev(s[:-1])
s='oho'
print(rev(s))
revs=rev(s)
if s==revs:
    print(True)
else:
    print(False)    