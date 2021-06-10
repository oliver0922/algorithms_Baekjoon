import sys
from collections import deque
n=int(sys.stdin.readline())
queue=deque()
limit_five=0
limit_three=0
while (5*limit_five)<=n:
    limit_five+=1
while (3*limit_three)<=n:
    limit_three+=1    

for i in range(limit_five):
    for j in range(limit_three):
        if n==5*i+3*j:
            queue.append(i+j)
    
       
if len(queue)!=0:
    print(min(queue))
else:
    print(-1)
