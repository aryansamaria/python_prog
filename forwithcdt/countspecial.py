s=input()
count=0
for i in s:
    if i.isalnum()==False:
        count+=1
print(count)        