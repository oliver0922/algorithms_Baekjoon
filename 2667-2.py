import sys
from collections import deque

def bfs(V):
    dq=deque()
    visited[V]=True
    dq.append(V)
    while len(dq)!=0:
        a=dq.popleft()
        for i in Map[a]:
            if not visited[i]:
                dq.append(i)
                dq[i]=0


N=int(sys.stdin.readline())
Map=[]
visited=[[False for i in range(N)] for i in range(N)]
for i in range(N):
    row=list(map(int,sys.stdin.readline().split()))
    Map.append(row)
dx=[-1,1,0,0]
dy=[0,0,-1,1]
now=[0,0]
for i in range(N):
    for j in range(N):
        now=[i][j]
        for i in range(4):
            x=now[0]+dx[i]
            y=now[1]+dy[i]

            if visited[x][y] ==1 and -1<x<N and -1<y<N:
                visited[x][y]=0









