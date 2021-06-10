import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())
adj_list=[[]for i in range(N+1)]
visited=[False]*(N+1)
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    adj_list[b].append(a)
count=[0]
idx=[0]


def bfs(V):
    cnt=1
    dq=deque()
    visited[V]=True
    dq.append(V)

    while len(dq)!=0:
        a=dq.popleft()
        for i in adj_list[a]:
            if not visited[i]:
                visited[i]=True
                cnt+=1
                dq.append(i)
    return cnt

for i in range(1,N+1):
    b=bfs(i)
    visited=[False]*(N+1)
    if b>count[-1]:
        while len(count)!=0:
            count.pop()
            idx.pop()
        count.append(b)
        idx.append(i)    
    elif b==count[-1]:
        count.append(b)
        idx.append(i)   
    else:
        continue

for i in idx:
    print(i,'',end='')






