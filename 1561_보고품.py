import sys

N,M=map(int,sys.stdin.readline().split())
time=list(map(int,sys.stdin.readline().split()))


if N<M:
    print(N)
else:
    start=0
    end=N*30

    while start<=end:
        sum=M
        mid=(start+end)//2
        for i in time:
            sum+=mid//i

        if sum>=N:
            end=mid-1

        else:
            start=mid+1

    

    

    sum_2=M #마지막 시간 직전까지 합친 학생 수
    for i in time:
        sum_2+=(mid-1)//i
    

    for i in range(M):
        if mid%time[i]==0:
            sum_2+=1
        if sum_2==N:
            print(i+1)
            break
       

 

