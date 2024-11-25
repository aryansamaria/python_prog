s=input()
count=0
# d={'0':0}
for i in s:
    if i.isdigit():
        if int(i)%2==0:
            count+=1
print(count)        