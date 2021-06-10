import sys

def dfs(v):
    visited[v]=True
    for i in adj_list[v]:
        if not visited[i]:
            dfs(i)
    










N,M=map(int,sys.stdin.readline().split())
adj_list=[[]for i in range(N+1)]
visited=[False]*(N+1)
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

flag=0
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        flag+=1
print(flag)
