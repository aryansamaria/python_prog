s=input()
count=0
v='aeiou'
for i in s.lower():
    if i.isalpha() and i not in v:
        count+=1
print(count)        