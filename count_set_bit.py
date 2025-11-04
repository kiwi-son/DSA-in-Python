def count(n):
    cnt=0
    
    while(n>1):
        if(n%2==1):
            cnt+=1
        n=n>>1 #right shift means divide by 2
        #print(n) 
        if n==1:
            cnt+=1
    return cnt

def count2(n):
    cnt=0
    while n>0:
        n= n& n-1
        cnt+=1
    return cnt
print(count2(15))

