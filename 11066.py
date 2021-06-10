import sys


T=int(sys.stdin.readline())

for i in range(T):
    K=int(sys.stdin.readline())
    candidate=list(map(int,sys.stdin.readline().split()))
    dp=[[0 for i in range(K+1)] for j in range(K+1)]

    for i in range(K):
        dp[i+1][i+1]=candidate[i]

    for i in range(1,K):
        dp[i][i+1]=dp[i][i]+dp[i+1][i+1]

   
    cost=[]
    for a in range(2,K):
        for i in range(1,K-a+1):
            minimum=dp[i][i]+dp[i+1][i+a]
            for j in range(i,a+i):
                if dp[i][j]+dp[j+1][i+a]<minimum:
                    minimum=dp[i][j]+dp[j+1][i+a]
            dp[i][i+a]=minimum
    print(dp)
    

            
    

    
        
