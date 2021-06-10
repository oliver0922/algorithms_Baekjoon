import sys

N,C=map(int,sys.stdin.readline().split())
house=[]
for i in range(N):
    a=int(sys.stdin.readline())
    house.append(a)

house.sort()
start=
end=house[-1]-house[0]


while start<=end:
    count=1
    old=house[0]
    mid=(start+end)//2

    for i in range(1,N):
        if old+mid<=house[i]:
            count+=1
            old=house[i]

    if count>=C:
        answer=mid
        start=mid+1
    else:
        end=mid-1


print(answer)
