import sys
from collections import deque


def bfs(v):
    visited[v]=True
    queue=deque()
    queue.append(v)
    counted=1
    while len(queue)!=0:
        a=queue.popleft()
        print(a)
        if len(adj_list[a])!=0:
            counted=counted-(len(adj_list[a])-1)
        for i in adj_list[a]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                counted+=1
    print(counted)
    



N,M=map(int,sys.stdin.readline().split())
matrix=[]
visited=[False]*(N*M+1)
adj_list=[[]for i in range(N*M+1)]
cnt=1
for i in range(N):
    a=list(map(int,sys.stdin.readline().rstrip()))
    for i in range(M):
        if a[i]==1:
            a[i]=cnt
            cnt+=1
    matrix.append(a)


for i in range(1,N-1):
    for j in range(1,M-1):
        if matrix[i][j]!=0:
            if matrix[i-1][j]!=0:
                adj_list[matrix[i][j]].append(matrix[i-1][j])
            if matrix[i+1][j]!=0:
                adj_list[matrix[i][j]].append(matrix[i+1][j])
            if matrix[i][j-1]!=0:
                adj_list[matrix[i][j]].append(matrix[i][j-1])
            if matrix[i][j+1]!=0:
                adj_list[matrix[i][j]].append(matrix[i][j+1])

for j in range(1,M-1):
    if matrix[0][j]!=0:
            if matrix[1][j]!=0:
                adj_list[matrix[0][j]].append(matrix[1][j])
            if matrix[0][j-1]!=0:
                adj_list[matrix[0][j]].append(matrix[0][j-1])
            if matrix[0][j+1]!=0:
                adj_list[matrix[0][j]].append(matrix[0][j+1])
    if matrix[N-1][j]!=0:
            if matrix[N-2][j]!=0:
                adj_list[matrix[N-1][j]].append(matrix[N-2][j])
            if matrix[N-1][j-1]!=0:
                adj_list[matrix[N-1][j]].append(matrix[N-1][j-1])
            if matrix[N-1][j+1]!=0:
                adj_list[matrix[N-1][j]].append(matrix[N-1][j+1])

for i in range(1,N-1):
    if matrix[i][0]!=0:
        if matrix[i-1][0]!=0:
            adj_list[matrix[i][0]].append(matrix[i-1][0])
        if matrix[i+1][0]!=0:
            adj_list[matrix[i][0]].append(matrix[i+1][0])
        if matrix[i][1]!=0:
            adj_list[matrix[i][0]].append(matrix[i][1])
    if matrix[i][M-1]!=0:
        if matrix[i-1][M-1]!=0:
            adj_list[matrix[i][M-1]].append(matrix[i-1][M-1])
        if matrix[i+1][M-1]!=0:
            adj_list[matrix[i][M-1]].append(matrix[i+1][M-1])
        if matrix[i][M-2]!=0:
            adj_list[matrix[i][M-1]].append(matrix[i][M-2])

if matrix[0][1]!=0:
    adj_list[matrix[0][0]].append(matrix[0][1])
if matrix[1][0]!=0:
    adj_list[matrix[0][0]].append(matrix[1][0])

if matrix[N-1][1]!=0:
    adj_list[matrix[N-1][0]].append(matrix[N-1][1])
if matrix[N-2][0]!=0:
    adj_list[matrix[N-1][0]].append(matrix[N-2][0])


if matrix[0][M-2]!=0:
    adj_list[matrix[0][M-1]].append(matrix[0][M-2])
if matrix[1][M-1]!=0:
    adj_list[matrix[0][M-1]].append(matrix[1][M-1])

if matrix[N-1][M-2]!=0:
    adj_list[matrix[N-1][M-1]].append(matrix[N-1][M-2])
if matrix[N-2][M-1]!=0:
    adj_list[matrix[N-1][M-1]].append(matrix[N-2][M-1])


bfs(i)





