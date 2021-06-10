import sys

a=list(sys.stdin.readline().rstrip().split('-'))
plus=[]
for i in a:
    b=list(i.split('+'))
    sum=0
    for c in b:
        sum+=int(c)
    plus.append(sum)
ans=plus[0]
for i in range(1,len(plus)):
    ans-=plus[i]
print(ans)

    
    


