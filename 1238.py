import sys


N,M,X=map(int,sys.stdin.readline().split())#N=학생 수, X=모이기로 한 마을 M= 경로 갯수
g=[]
for i in range(1,N+2):
    g.append([])

for i in range(1,M+1):
    start,stop,weight=map(int,sys.stdin.readline().split())
    g[start].append((stop,weight))

def dijkstra(start):
    visited=[False]*(N+1)
    D=[sys.maxsize]*(N+1)
    D[start]=0
    for k in range(N):
        m=-1
        min_value=sys.maxsize
        for j in range(1,N+1):
            if not visited[j] and D[j]<min_value:
                min_value=D[j]
                m=j
        visited[m]=True
        for w,wt in list(g[m]):
            if not visited[w]:
                if D[m]+wt<D[w]:
                    D[w]=D[m]+wt
    D[0]=0
    return D
a=dijkstra(X)

for i in range(1,N+1):
    a[i]+=dijkstra(i)[X]
print(max(a))
    
