import sys

N=int(sys.stdin.readline())

vocalist=[]
voca_dict={}

for i in range(N):
    eachlist=list(sys.stdin.readline().rstrip())
    vocalist.append(eachlist)


for each_list in vocalist:
    for i in range(len(each_list)):
        if not each_list[i] in voca_dict:
            voca_dict[each_list[i]]=10**(len(each_list)-i-1)
        else:
            voca_dict[each_list[i]]+=10**(len(each_list)-i-1)

voca_dict=sorted(voca_dict.values(),reverse=True)

sum=0
num=9
for i in voca_dict:
    sum+=num*i
    num-=1

print(sum)
