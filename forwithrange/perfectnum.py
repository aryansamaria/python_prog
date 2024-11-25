n=int(input())
sum=0
for num in range(1,n):
    if num%n==0:
        sum+=num
if sum==num:
    print("perfect")
else:
    print("not perfect")            
