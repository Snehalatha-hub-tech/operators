#square pattern
r,c=map(int,input().split())
for i in range(r):
    for j in range(c):
        print("*",end=" ")
    print()
    
r,c=map(int,input().split())
for i in range(r):
    for j in range(c):
        print(j+1,end=" ")
    print()
    
r,c=map(int,input().split())
for i in range(r):
    for j in range(c):
        print(i+1,end=" ")
    print()
    
n=int(input())
num=1
for i in range(n):
    for j in range(n):
        print(num,end=" ")
        num+=1
    print()
    
r=int(input())
for i in range(r):
    for j in range(r):
        if(j<i+1):
            print("*",end=" ")
    print()
    
n=int(input())
for i in range(n):
    for j in range(n):
        if (i<j+1):
            print("*",end=" ")
    print() 
n=int(input())
for i in range(n):
    for j in range(n):
        if (j<i+1):
            print(j+1,end=" ")
    print()
    
n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
#hallow square
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#hallow right angle triangle
n=int(input())
for i in range(n):
    for j in range (n):
         if i==n-1 or j==0 or i==j:
             print("*",end=" ")
         else:
             print(" ",end=" ")
    print()
    
n=int(input())
for i in range(n):
    if i %2 == 0:
        for j in range(n):
            print("*",end=" ")
    else:
             for j in range(n):
                 print("+",end=" ")
    print()
    
n=int(input())
for i in range(1,n):
    print(" "*(n-i) + "*"*i)
for i in range(n,0,-1):
    print(" "*(n-i) + "*"*i)
n=int(input())
for i in range(n):
    for j in range(n):
        if i == 0 or i ==n-1 or  j == 0 or i == n//2:
            print("*",end=" ")
    print()
    
n=int(input())
for i in range(n):
    for j in range(n):
        if i == 0 or i == n//2 or i == n-1:
            print("*",end=" ")
        elif i <n//2 and j==0:
            print("*",end=" ")
        elif j == n-1 and i>n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()
        
    
            
    
    
             

    

    
        
