nums=[1,2,3]
n=len(nums)

sub=1<<n
ans=[]
for i in range(sub):
    l=[]
    for j in range(n):
        if i & (1<<j):
            l.append(nums[j])

    ans.append(l)

print(ans)