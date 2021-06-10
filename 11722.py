import sys

N=int(sys.stdin.readline())
lst=list(map(int,sys.stdin.readline().split()))
dp=[1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if lst[j]>lst[i]:
            dp[i]+=dp[j]
    
print(dp)
