import sys


def ccw(a):
    b= (a[1][0]*a[2][1]-a[2][0]*a[1][1])-(a[0][0]*a[2][1]-a[2][0]*a[0][1])+(a[0][0]*a[1][1]-a[1][0]*a[0][1])

    if b<0:
        return -1
    elif b==0:
        return 0
    else:
        return 1
    

point=[]
for _ in range(3):
    a,b=map(int,sys.stdin.readline().split())
    point.append([a,b])


print(ccw(point))
    
