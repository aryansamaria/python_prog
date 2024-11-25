l=[11,22,33,44,55,66]
for i in range(len(l)//2):
    l[i],l[len(l)-i-1]=l[len(l)-i-1],l[i]
print(l)    