import sys

S,E,Q=map(str,sys.stdin.readline().split())

S=int(S[0:2]+S[3:5])
E=int(E[0:2]+E[3:5])
Q=int(Q[0:2]+Q[3:5])


income={}
outcome={}
while True:
    log=sys.stdin.readline().strip()
    if len(log)<5:
        break
    time,nickname=map(str,log.split())
    time=int(time[0:2]+time[3:5])
    if time<=S:
        income[nickname]=time
    elif E<=time<=Q:
        outcome[nickname]=time
    else:
        continue



count=0
for i in income:
    if i in outcome:
       count+=1

print(count)
