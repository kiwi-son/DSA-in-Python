s=12
g=17

n=s^g
cnt=0
while n>0:
    n=n&n-1
    cnt+=1

print(cnt)