import sys
from collections import deque
def dfs(V):
    visited[V]=True
    print(V,'',end='')

    for i in adj_list[V]:
        if not visited[i]:
            dfs(i)

def bfs(V):
    visited[V]=True
    dq.append(V)

    while len(dq)!=0:
        a=dq.popleft()
        print(a,'',end='')
        for i in adj_list[a]:
            if not visited[i]:
                dq.append(i)
                visited[i]=True

N,M,V=map(int,sys.stdin.readline().split())

adj_list=[[]for i in range(N+1)]
dq=deque()
visited=[False]*(N+1)

for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
for i in range(1,N+1):
    adj_list[i].sort()

dfs(V)

print()

visited=[False]*(N+1)
bfs(V)


    


    

