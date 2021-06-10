import sys
from collections import deque
n=int(sys.stdin.readline())
building=deque()

cnt=0
for i in range(n):
    a=int(sys.stdin.readline())
    while True:
        if len(building)==0 or building[-1]>a:
            building.append(a)
            cnt+=len(building)-1
            break
        else:
            building.pop()


print(cnt)

