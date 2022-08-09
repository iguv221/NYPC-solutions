from sys import stdin
import random
input = lambda:stdin.readline().rstrip()

Size = int(input())
Grid=[]
c_count=0
d_count=0
for _ in range(Size):
    t = list(input())
    for i in t:
        if i=='C':
            c_count+=1
        elif i=='D':
            d_count+=1
    Grid.append(t)

more = max(0,c_count*2-d_count)

if more!=0:
    ### 매우 단순하게
    # Stop=False
    # for line in Grid:
    #     for i in range(Size):
    #         if line[i]=='.': 
    #             line[i]='D'
    #             more-=1
    #             if more==0:
    #                 Stop=True
    #         if Stop:
    #             break
    #     if Stop:
    #         break

    ### 랜덤하게
    while more>0:
        x = random.randint(0,Size-1)
        y = random.randint(0,Size-1)
        if Grid[y][x]=='.':
            Grid[y][x]='D'
            more-=1

for i in Grid:
    print("".join(i))
