import sys

N,M=map(int,sys.stdin.readline().split())

tree_height=list(map(int,sys.stdin.readline().split()))

start=0
end=max(tree_height)

while start<=end:
    sum=0
    mid=(start+end)//2

    for i in tree_height:
        if i-mid>0:
            sum+=(i-mid)

    if sum>=M:
        answer=mid
        start=mid+1

    else:
        end=mid-1


print(answer)
        
