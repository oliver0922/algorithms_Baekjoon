import sys
from collections import deque





n=int(sys.stdin.readline())
a=deque(map(int,sys.stdin.readline().split()))
sum_list=deque()
a.sort()

for i in range(1,len(a)+1):
    cnt=1
    ssum=0
    while cnt<=i:
        ssum+=a[cnt-1]
        cnt+=1
    sum_list.append(ssum)

print(sum(sum_list))
