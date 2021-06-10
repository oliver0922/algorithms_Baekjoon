import sys

N=int(sys.stdin.readline())
candidate=[]
for i in range(N):
    a=list(map(int,sys.stdin.readline().split()))
    candidate.append(a)


candidate.sort(key=lambda x:(x[1],x[0]))


ans=[candidate[0]]
for i in range(1,N):
    if candidate[i][0]>=ans[-1][1]:
        ans.append(candidate[i])
           

print(len(ans))            
    
