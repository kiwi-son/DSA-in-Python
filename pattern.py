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
