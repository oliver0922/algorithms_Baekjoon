import sys

n=int(sys.stdin.readline())
list_meeting=[]

for i in range(n):
    a=list(map(int,sys.stdin.readline().split()))
    list_meeting.append(a)
print(list_meeting)
list_meeting.sort(key=lambda x:(x[1],x[0]))
print(list_meeting)

endtime=0
cnt=0
for i in range(n):
    if endtime<=list_meeting[i][0]:
        endtime=list_meeting[i][1]
        cnt+=1
print(cnt)


