import sys


T=int(sys.stdin.readline())
total=[]
s=[]
for i in range(T):
    N=int(sys.stdin.readline())
    s=[]
    for j in range(N):
        [a,b]=list(map(int,sys.stdin.readline().split()))
        s.append([a,b])
    s.sort(key=lambda x:x[0])
    minimum=s[0][1]
    cnt=1
    for k in range(1,N):
        if s[k][1]<=minimum:
            cnt+=1
            minimum=s[k][1]
    print(cnt)

            
        
    



