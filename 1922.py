import sys
from collections import deque
N,M=map(int,(sys.stdin.readline().split())) 
candidate=[] #노드1,노드2,가중치를 담는 리스트
parent=[None]*(N+1)  #노드의 부모노드를 담는 노드
mst_cost=0   #최소신장트리 가중치 합
tree_edges=0 #트리의 간선 갯수
D=[]
for i in range(M):
    Node1,Node2,weight=map(int,sys.stdin.readline().split())
    candidate.append((Node1,Node2,weight))
    parent[Node1]=Node1
    parent[Node2]=Node2
candidate.sort(key=lambda x:x[2])
candidate=deque(candidate)

def find(u):    #루트노드를 찾는 find 함수, u=노드
    if u!=parent[u]:
        parent[u]=find(parent[u]) #경로 압축
    return parent[u]

def union(u,v): #2개의 집합을 하나의 집합으로 만드는 union 함수, u,v=노드
    root1=find(u)
    root2=find(v)
    parent[root2]=root1 #root2의 부모를 root1이 되게 만든다.

while True:
    if tree_edges == N-1: 
        break
    u,v,wt=candidate.popleft() #최소 가중치를 가진 노드1,노드 2 간선 추출
    if find(u)!=find(v): #u와 v가 서로 다른 집합에 속해있으면
        union(u,v)
        mst_cost+=wt
        tree_edges+=1
        D.append(wt)

print(mst_cost-max(D))
