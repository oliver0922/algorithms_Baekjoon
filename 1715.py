import sys
import heapq
N=int(sys.stdin.readline())


h=[]
sum=0

for i in range(N):
    a=int(sys.stdin.readline())
    h.append(a)

heapq.heapify(h)

if N==1:
    print(0)
else:
    while len(h)!=1:
        a1=heapq.heappop(h)
        a2=heapq.heappop(h)
        sum=a1+a2+sum
        heapq.heappush(h,a1+a2)

    print(sum)
