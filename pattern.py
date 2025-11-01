#Square Pattern
"""
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
"""

def square_pattern(n):
    for i in range(1,n+1):
        for j in range (1, n+1):
            print(j," ",end="")
        print("\n", end ="")
        
"""
A B C D
A B C D
A B C D
A B C D 
"""
def square_char(n):
    for i in range(1,n+1):
        for j in range(0, n):
            print(chr(65+j)," ",end="")
        print("\n",end="")
        
n=int(input("Enter the number"))
square_pattern(n)
square_char(n)

"""
1 2 3
4 5 6
7 8 9
"""

def square_pat(n):
    x=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            x+=1
            print(x," ",end="")
        print("\n",end="")

print(square_pat(n))

"""
*
* *
* * *
* * * *
"""

def tri(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("* ",end="")
        print("\n",end="")
print(tri(n))

"""
1
2 2
3 3 3
4 4 4 4
"""
def num_tri(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i," ",end="")
        print("\n",end="")
num_tri(n)

"""
1
1 2
1 2 3
1 2 3 4
"""

def num_tri2(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j," ", end="")
        print("\n",end="")

num_tri2(n)
"""
1
2  1
3  2  1
4  3  2  1
"""
def rev_tri(n):
    for i in range(1,n+1):
        for j in range(i,0,-1):
            print(j," ", end="")
        print("\n",end="")


rev_tri(n)

def floyed_tri(n):
    x=0
    for i in range(n):
        for j in range(0,i+1):
            x+=1
            print(x," ",end="")
        print("\n",end="")

floyed_tri(n)

def invert(n):
    for i in range(1,n+1):
        for k in range(i-1):
            print("   ",end="")
        for j in range(n+1-i,0,-1):
            print(i," ",end="" )
        print("\n",end="")

invert(n)
