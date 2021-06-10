import sys
from collections import deque

M,N=map(int,sys.stdin.readline().split())
s=[]
idx=[]

for i in range(N):
    row=list(map(int,sys.stdin.readline().split()))
    s.append(row)


for i in range(M):
    for j in range(N):
        if s[j][i]==1:
            idx.append([j,i])

def bfs(idx):
    cnt=-1
    
    dq=deque(idx)
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while len(dq)!=0:
        cnt+=1
        for _ in range(len(dq)):
            now=dq.popleft()
            

            for i in range(4):
                y=now[0]+dy[i]
                x=now[1]+dx[i]

                if 0<=x<M and 0<=y<N:
                    if s[y][x]==0:
                        s[y][x]=1
                        dq.append([y,x])
                    
    for i in s:
        for j in i:
            if j==0:
                return -1
    
    return cnt
                
    

print(bfs(idx))


