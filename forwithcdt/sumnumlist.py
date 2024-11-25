l=[33,11,22,'hai','22',[23,34]]
sum=0
for i in l:
    if type(i)==int:  #isinstance(i,int)
        sum+=i
print(sum)        