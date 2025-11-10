def single(l):
    
    l.sort()
    for i in range(1,len(l),3):
        if l[i]!=l[i-1]:
            return l[i-1]
    return l[-1]


l=[1,2,3,3,3,2,2]
print(single(l))