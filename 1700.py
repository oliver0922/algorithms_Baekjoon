import sys
from collections import deque

N,K=map(int,sys.stdin.readline().split())
candidate=deque(map(int,sys.stdin.readline().split()))
multitab=[0]*N
cnt=0


while len(candidate)!=0:
    new=candidate.popleft()
    if new in multitab:
        continue
    flag=0
    for i in range(N):
        if multitab[i]==0:
            multitab[i]=new
            flag+=1
            break
    if flag==1:
        continue
    

    for i in range(N):
        if not multitab[i] in candidate:
            multitab[i]=new
            cnt+=1
            flag+=1
            break
    if flag==1:
        continue
        
    index=0
    max=-1
    for i in range(N):
        num=candidate.index(multitab[i])
        if max<num:
            max=num
            index=i
    multitab[index]=new
    cnt+=1


print(cnt)
            
