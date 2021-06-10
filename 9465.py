import sys

T=int(sys.stdin.readline())
for _ in range(T):
    n=int(sys.stdin.readline())
    candidate=[]
    for i in range(2):
        a=list(map(int,sys.stdin.readline().split()))
        candidate.append(a)

    dp=[0 for i in range(1000001)]
    dp[1]=max(candidate[0][0],candidate[1][0])
    if n>=2:
        dp[2]=max(candidate[0][0]+candidate[1][1],candidate[1][0]+candidate[0][1])

    

    for i in range(3,n+1):
        if dp[i-2]-dp[i-3]==candidate[0][i-3]:
            dp[i]=dp[i-2]+max(candidate[1][i-1],candidate[0][i-1]+candidate[1][i-2])
        elif dp[i-2]-dp[i-3]==candidate[1][i-3]:
            dp[i]=dp[i-2]+max(candidate[0][i-1],candidate[1][i-1]+candidate[0][i-2])
        else:
            dp[i]=dp[i-3]+max(candidate[0][i-1]+candidate[1][i-2],candidate[1][i-1]+candidate[0][i-2])

    print(dp[3])
      
