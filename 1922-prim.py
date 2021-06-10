import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())
candidate = []
for i in range(N+1):
    candidate.append([])

for i in range(M):
    Node1,Node2,weight=map(int,sys.stdin.readline().split())
    candidate[Node1].append((Node2,weight))
    candidate[Node2].append((Node1,weight))

visited = [False]*(N+1)  # 초기화
D = [1000]*(N+1)  # D[i]를 최댓값으로 초기화


for k in range(N):     
    m = -1
    min_value = 1001
    for j in range(1,N+1): # 방문안된 정점들의 D 원소들 중에서 최솟값을 가진 정점 m 찾기
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j           
    visited[m] = True  
    for w, wt in candidate[m]: # m에 인접한 방문 안된 각 정점의 D의 원소 갱신           
        if not visited[w]:  
            if wt < D[w]:             
                D[w] = wt  # D 원소 갱신

mst_cost = 0 #최소신장 트리 가중치 
for i in range(1,N):
    mst_cost += D[i]
print(mst_cost-max(D))
