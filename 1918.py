class Lstack:
    class Node:
        def __init__(self,item,link):
            self.item=item
            self.next=link

    def __init__(self):
        self.top=None
        self.size=0
    def push(self,item):
        self.top=self.Node(item,self.top)
        self.size+=1

    def peek(self):
        if self.size !=0:
            return self.top.item

    def pop(self):
        if self.size !=0:
            top_item=self.top.item
            self.top=self.top.next
            self.size-=1
            return top_item

    def print_stack(self):
        print('top ->\t',end='')
        p=self.top
        while p:
            if p.next !=None:
                print(p.item,'->',end='')
            else:
                print(p.item)
            p=p.next

ls=Lstack()
s=list(input())

for i in range(len(s)):
    if ((s[i]=='*') or (s[i]=='/')):
        if ls.top == None:
            ls.push(s[i])
        else:
            while ((ls.top.item != '+') and (ls.top.item!='-') and (ls.top.item!='(')):
                print(ls.pop(),end='')
                if ls.size ==0: break
            ls.push(s[i])
    elif (( s[i]== '+') or (s[i]=='-')):
        if ls.top == None:
            ls.push(s[i])
        else:
            while ((ls.top!=None) and (ls.top.item!='(')):
                print(ls.pop(),end='')
            ls.push(s[i])

    elif s[i]=='(':
        ls.push(s[i])
    elif s[i]==')':
        p=ls.pop()
        while (p!='('):
            print(p,end='')
            p=ls.pop()
    else:
        print(s[i],end='')


    
while ls.size!=0:
        print(ls.pop(),end='')
