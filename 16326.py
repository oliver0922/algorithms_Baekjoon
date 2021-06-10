import sys
from collections import deque

class shark:
    def __init__(self,row,col,size=2,eat=0):
        self.eat=0 #먹은 횟수
        self.size=size#상어 크기
        self.row=row#상어 위치 행
        self.col=col#상어 위치 열
        
N=int(sys.stdin.readline())
a=[]#전체 지도 나타냄
candidate=[]#먹을 수 있는 후보

for i in range(N):
    b=list(map(int,sys.stdin.readline().split()))
    if 9 in b:
        start_row,start_col=i,b.index(9) #아기상어 위치찾기(행,렬)
    a.append(b)

shark=shark(start_row,start_col)


flag=0
cnt=0


while True:
    
    for i in range(N):
        for j in range(N):
            if (a[i][j]<shark.size) and (a[i][j]!=0):
                candidate.append([i,j,a[i][j]])
    

    if len(candidate)!=0: # 먹을 수 있는 후보가 있을 때
        flag+=1
        candidate.sort(key=lambda x:(x[2],x[0],x[1]))

        while True:

            if len(candidate)==0 
                print(cnt)
                break
            
            fish=candidate.pop(0)
            if fish[2]>shark.size:
                print(cnt)
                break

            #물고기 먹으러가기
            if shark.row>fish[0] and shrak.col<fish[1]:
                


            elif shark.row<fish[0] and shrak.col<fish[1]:


            elif shark.row>fish[0] and shrak.col>fish[1]:


            else:
                
            
            
        
                
        




    else:#먹을 수 있는 후보가 없을때
        break




if flag==0:
    print(0)
    








