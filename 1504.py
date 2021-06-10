import sys

N,E=map(int,sys.stdin.readline().split())
g=[[] for i in range(N+1)]


for i in range(E):
    start,stop,weight=map(int,sys.stdin.readline().split())
    g[start].append((stop,weight))
    g[stop].append((start,weight))

v1,v2=map(int,sys.stdin.readline().split())

def dijkstra(start,dest):
    D=[sys.maxsize]*(N+1)
    D[start]=0
    visited=[False]*(N+1)

    for i in range(N):
        m=-1
        min_value=sys.maxsize

        for j in range(1,N+1):
            if not visited[j] and D[j]<min_value:
                min_value=D[j]
                m=j
        visited[m]=True
        for stop,weight in list(g[m]):
            if not visited[stop]:
                if D[m]+weight<D[stop]:
                    D[stop]=D[m]+weight
    return D[dest]



candidate_1=dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,N)
candidate_2=dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,N)
ans=min(candidate_1,candidate_2)
if ans<sys.maxsize:
    print(ans)
else:
    print(-1)
