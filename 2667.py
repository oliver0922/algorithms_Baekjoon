import sys
from collections import deque

N=int(sys.stdin.readline())
mapp=[]
for i in range(N):
    a=list(map(int,sys.stdin.readline().rstrip()))
    mapp.append(a)

dx=[-1,1,0,0]
dy=[0,0,-1,1]
result=[]
def bfs(i,j):
    cnt=1
    queue=deque([[i,j]])
    mapp[i][j]=0
    while len(queue)!=0:
        a,b=queue[0][0],queue[0][1]
        queue.popleft()

        for i in range(4):
            x=a+dx[i]
            y=b+dy[i]

            if 0<=x<N and 0<=y<N and mapp[x][y]==1:
                queue.append([x,y])
                mapp[x][y]=0
                cnt+=1
    result.append(cnt)

for i in range(N):
    for j in range(N):
        if mapp[i][j]==1:
            bfs(i,j)
            
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])            
