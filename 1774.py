import sys
import math
from collections import deque


N,M=map(int,sys.stdin.readline().split())
location=[] #좌표 저장리스트
candidate=[]
parent=[0]
mst_tree=[]
mst_cost=0
tree_edges=M
already=0

for i in range(1,N+1):
    parent.append(i)

def find(u):
    if parent[u]!=u:
        parent[u]=find(parent[u])
    return parent[u]

def union(u,v):
    root1=find(u)
    root2=find(v)
    if root2<root1:
        parent[root2]=root1
    else:
        parent[root1]=root2

for i in range(N):
    x,y=map(int,sys.stdin.readline().split()) #좌표 값  받기
    location.append((x,y,i+1))#x좌표 y좌표 노드번호

for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    weight=math.sqrt((location[a-1][0]-location[b-1][0])**2+(location[a-1][1]-location[b-1][1])**2)
    mst_cost+=weight
    union(a,b)
    mst_tree.append((a,b,weight))
    already+=weight

for i in range(N-1):
    for j in range(i+1,N):
        distance=math.sqrt((location[i][0]-location[j][0])**2+(location[i][1]-location[j][1])**2)
        candidate.append((i+1,j+1,distance))
candidate.sort(key=lambda x:x[2])
candidate=deque(candidate)

print(candidate)
for u,v,wt in candidate:
    if find(u)!=find(v):
        union(u,v)
        mst_tree.append((u,v))
        mst_cost+=wt
        tree_edges+=1
print(parent)           
print(format(mst_cost-already,".2f"))
