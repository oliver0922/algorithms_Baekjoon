import sys
from collections import deque


T=int(sys.stdin.readline())
for i in range(T):
    N,K=map(int,sys.stdin.readline().split()) #N=건물의 갯수,#K=건설순서 규칙
    indegree=[0]*(N+1)
    queue=deque()
    adj_list=[[] for _ in range(N+1)]
    time=list(map(int,sys.stdin.readline().split()))
    for _ in range(K):
        X,Y=map(int,sys.stdin.readline().split())
        adj_list[X].append(Y)
        indegree[Y]+=1

    for i in range(1,N+1): #시작 점 큐에 집어넣기
        if indegree[i]==0:
            queue.append(i)
   
    W=int(sys.stdin.readline())
    #a=[]
    for i in range(N):
        if not queue:
            pass
        else:
            cur=queue.popleft()
            maximum=0
            for k in range(1,N+1):
                if cur in adj_list[k]:
                    if time[k-1]>maximum:
                        maximum=time[k-1]
            time[cur-1]=maximum+time[cur-1]                               
            for j in adj_list[cur]:
                indegree[j]-=1
                if indegree[j]==0:
                    queue.append(j)
    print(time[W-1])
                    
   
    
                
        
    

   
