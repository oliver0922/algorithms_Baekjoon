import sys
from collections import deque

N=int(sys.stdin.readline())


h=[]
sum=0

for i in range(N):
    a=int(sys.stdin.readline())
    h.append(a)

h=deque(h)
sum=0
if N==1:
    print(h[0])

else:
    while len(h)!=1:
        a1=h.popleft()
        a2=h.popleft()
        sum=sum+a1+a2
        h.appendleft(a1+a2)

    print(sum)
    
