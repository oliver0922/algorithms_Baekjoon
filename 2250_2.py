import sys
from collections import deque

class Node:
    def __init__(self,item,left=None,right=None,x=None,y=None):
        self.item=item
        self.left=left
        self.right=right
        self.x=x #level
        self.y=y #row
          
class BinaryTree:
    def __init__(self):
        self.root=None

    def row(self,n,depth): #노드 열번호 붙여주기
        global cnt
        if n!=None:
            n.x=depth
            if n.left!=None:
                self.row(n.left,depth+1)
            n.y=cnt
            cnt+=1
            if n.right!=None:
                self.row(n.right,depth+1)
                                    

    def height(self,n): #높이 찾기
        if n==None:
            return 0
        return max(self.height(n.left),self.height(n.right))+1

    def level(self,root,height): #여기 모르겠:
        queue=deque()
        queue.append(root)
        global cnt_row
        #root.x=cnt_row
        
        b=1

        for i in range(0,height):
            if i==0:
                b=1 #pop횟수
            else:
                b*=2

            for j in range(b):
                if len(queue)!=0:
                    a=queue.popleft()
                    if a!=None:
                        queue.append(a.left)
                        queue.append(a.right)
                        a.x=cnt_row
                    else:
                        queue.append(None)
                        queue.append(None)
            cnt_row+=1
    

        
n=int(sys.stdin.readline())
a=[None]*100001 #Node담는 list


for i in range(1,n+1):
    a[i]=Node(i)

for i in range(n):
    n1,n2,n3=map(int,sys.stdin.readline().split())
    if n2!=-1:
        a[n1].left=a[n2]
    else:
        a[n1].left=None
    if n3!=-1:
        a[n1].right=a[n3]
    else:
        a[n1].right=None
    

cnt=1
cnt_row=1
BT=BinaryTree()
#루트 노드 찾기

for i in range(1,n+1):
    flag=0
    for j in range(1,n+1):
        if i!=j:
            if a[j].left==None and a[j].right==None:
                continue
            elif a[j].left!=None and a[j].right==None:
                if a[j].left.item==i:
                    flag=1
                    break
                else:
                    continue
            elif a[j].left==None and a[j].right!=None:
                if a[j].right.item==i:
                    flag=1
                    break
                else:
                    continue
            else:
                if a[j].left.item==i or a[j].right.item==i:
                    flag=1
                    break
                else:
                    continue
    if flag==0:
        BT.root=a[i]
        break


            
h=BT.height(BT.root)
BT.row(BT.root,1)



max_width=0
max_level=1


for i in range(1,h+1):
    width=[]
    for j in range(1,n+1):
        if a[j].x==i:
            width.append(a[j].y)
    candidate=max(width)-min(width)+1
    if candidate>max_width:
        max_width=candidate
        maxlevel=i

print(maxlevel,max_width)
    
    
