import sys
from collections import deque

def dfs(v):
    visited[v]=True
    print(v,'',end='')
    for i in adj_list[v]:
        if not visited[i]:
            visited[i]=True
            dfs(i)
        

def bfs(i):
    queue=[]
    queue.append(i)
    visited[i]=True
    while len(queue)!=0:
        v=queue.pop(0)
        print(v,'',end='')
        for w in adj_list[v]:
            if not visited[w]:
                visited[w]=True
                queue.append(w)
        
        

N,M,V=map(int,sys.stdin.readline().split())
adj_list=[[]for i in range(1001)]
visited=[False]*(1001)

for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
    adj_list[a].sort()
    adj_list[b].sort()
    




#dfs
'''
for i in range(V,1001):
    if not visited[i] and len(adj_list[i])!=0:
        dfs(i)
'''
dfs(V)
print()
#bfs
visited=[False]*(1001)
bfs(V)
'''
for i in range(V,1001):
    if not visited[i] and len(adj_list[i])!=0:
        bfs(i)
'''


