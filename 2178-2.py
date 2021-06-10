import sys
n, m = map(int, input().split())
s = []
queue = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    s.append(list(input()))
queue = [[0, 0]]
s[0][0] = 1
while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and s[x][y] == "1":
            queue.append([x, y])
            s[x][y] = s[a][b] + 1
print(s)




N,M=map(int,sys.stdin.readline().split())

mapp=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
queue=[[0,0]]

for i in range(N):
    a=list(map(int,sys.stdin.readline().rstrip()))
    mapp.append(a)

while len(queue)!=0:
    x=queue[0][0]
    y=queue[0][1]

    queue.pop(0)

    for i in range(4):
        a=x+dx[i] #index
        b=y+dy[i] #index

        if 0<=a<N and 0<=b<M and mapp[a][b]==1:
            mapp[a][b]=mapp[x][y]+1
            queue.append([a,b])

print(mapp)
