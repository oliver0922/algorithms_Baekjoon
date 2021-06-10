import sys

T=int(sys.stdin.readline())
for i in range(T):

    N=int(sys.stdin.readline())
    candidate=[]
    num=[]

    for j in range(N):
        a=list(map(int,sys.stdin.readline().split()))
        candidate.append(a)

    candidate.sort(key=lambda x:x[0])
    cnt=1
    min=candidate[0][1]
    for k in range(N):
        if candidate[k][1]<min:
            cnt+=1
            min=candidate[k][1]
            
            


    print(cnt)
        
    
