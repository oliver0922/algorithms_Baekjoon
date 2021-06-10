import sys


def find(u):
    if parent[u]!=u:
        parent[u]=find(parent[u])
    return parent[u]

def union(u,v):
    root1=find(u)
    root2=find(v)
    parent[root2]=root1

while True:
    m,n=map(int,sys.stdin.readline().split())
    if m==0 and n==0:
        break
    road=[]
    parent=[]
    sum=0
    tree_edges=0
    mst_cost=0
    for i in range(m):
        parent.append(i)

    for i in range(n):
        node1,node2,distance=map(int,sys.stdin.readline().split())
        road.append((node1,node2,distance))
        sum+=distance

    road.sort(key=lambda x:x[2])



    while True:
        if tree_edges==m-1:
            break
        for u,v,wt in road:
            if find(u)!=find(v):
                union(u,v)
                mst_cost+=wt
                tree_edges+=1

    print(sum-mst_cost)
