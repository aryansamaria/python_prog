s=input()
sum_ip=0
for ip in range(len(s)):
    if s[ip] in '02468':
        if ip%2==0:
            sum_ip+=ip
print(sum_ip)            