def sub(s):
    if not s:
        return set()
    print(s)
    s.pop()
    return sub(s)
s={1,2,3,4,5,6}
sub(s)