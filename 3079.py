import sys

N,M=map(int,sys.stdin.readline().split())
time=[]
for i in range(N):
    t=int(sys.stdin.readline())
    time.append(t)



start=1
end=M*10**9
sum=0

while start<=end:
    mid=(start+end)//2
    sum=0
    for i in time:
        sum+=(mid//i)
        if sum>=M:
            break

    if sum>=M:
        
        end=mid-1
        
    else:
        start=mid+1

print(mid)




            
