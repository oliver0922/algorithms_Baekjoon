import sys
from collections import deque

sum=0
a=deque()#최솟값
n,k=map(int,sys.stdin.readline().split())
for i in range(n):
    x=int(sys.stdin.readline())
    a.append(x)



for j in range(n-1,-1,-1):
    if k==0:
        break
    q=k//a[j]
    r=k%a[j]
    sum+=q
    k=r

print(sum)
        
