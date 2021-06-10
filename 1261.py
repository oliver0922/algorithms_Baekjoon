import sys

M,N=map(int,sys.stdin.readline().split()) #M가로크기 N세로크기
a=[[0]*M]*N
for i in range(N):
    b=list(map(int,sys.stdin.readline().rstrip()))
    a[i]=b

g=[[0]*M for _ in range(N)]


for i in range(1,M-1):
    g[0][i]=[(0,i-1,a[0][i-1]),(0,i+1,a[0][i+1]),(1,i,a[1][i])]
    g[N-1][i]=[(N-1,i-1,a[N-1][i-1]),(N-1,i+1,a[N-1][i+1]),(N-2,i,a[N-2][i])]

for j in range(1,N-1):
    g[j][0]=[(j-1,0,a[j-1][0]),(j+1,0,a[j+1][0]),(j,1,a[j][1])]
    g[j][M-1]=[(j-1,M-1,a[j-1][M-1]),(j+1,M-1,a[j+1][M-1]),(j,M-2,a[j][M-2])]

for i in range(1,N-1):
    for j in range(1,M-1):
        g[i][j]=[(i+1,j,a[i+1][j]),(i-1,j,a[i-1][j]),(i,j-1,a[i][j-1]),(i,j+1,a[i][j+1])]

if N>=2 and M>=2:
    g[0][0]=[(0,1,a[0][1]),(1,0,a[1][0])]
    g[N-1][0]=[(N-2,0,a[N-2][0]),(N-1,1,a[N-1][1])]
    g[0][M-1]=[(0,M-2,a[0][M-2]),(1,M-1,a[1][M-1])]
    g[N-1][M-1]=[(N-2,M-1,a[N-2][M-1]),(N-1,M-2,a[N-1][M-2])]
elif N==1 and M>=2:
    g[0][0]=[(0,1,a[0][1])]
    g[0][M-1]=[(0,M-2,a[0][M-2])]
elif N>=2 and M==1:
    g[0][0]=[(0,1,a[0][1])]
    g[N-1][0]=[(N-2,0,a[N-2][0])]
else:
    g[0][0]=[(0,1,a[0][1]),(1,0,a[1][0])]


  
def dijkstra():
    visited=[[False]*M for _ in range(N)]
    D=[[sys.maxsize]*M for _ in range(N)]
    D[0][0]=0
    for k in range(M*N):
        m=-1
        n=-1
        min_value=sys.maxsize
        for i in range(N):
            for j in range(M):
                if not visited[i][j] and D[i][j]<min_value:
                    min_value=D[i][j]
                    m,n=i,j
        visited[m][n]=True
        for row,col,wt in list(g[m][n]):
            if not visited[row][col]:
                if D[m][n]+wt<D[row][col]:
                    D[row][col]=D[m][n]+wt
    print(D[N-1][M-1])
                
                
dijkstra()       
     

        
