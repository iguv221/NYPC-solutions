from sys import stdin
input = lambda:stdin.readline().rstrip()

##   0
## 1   3
##   2

Dir = {'0':[0,-1],'1':[-1,0],'2':[0,1],'3':[1,0]}
Mirror = ['/','//']

Grid = []
X , Y = map(int,input().split())
for y in range(Y):
    t = list(input())
    for x in range(X):
        if t[x]=='\\':
            t[x]='//'
        elif t[x]=='O':
            start_y,start_x = y,x
    Grid.append(t)

ANSWERS = []

for D in range(4):
    now_y, now_x = start_y,start_x
    while (0<=now_y<Y and 0<=now_x<X):
        move_y, move_x = Dir[D]
        next_y, next_x = start_y + move_y , start_x + move_x
        if Grid[next_y][next_x] == '/':
            











# num=[]
# n=input() #문자열 받아오기
# for i in range(len(n)):
#     num.append((n[i]))
# sum=0 #소수의 개수

# #문자열 길이 최대 7
# #

# import itertools

# for t in range(1,len(n)+1):
#     print(t)
#     l=list(list(map(''.join, itertools.permutations(num,t))))
#     print(l)
#     l=list(set(l))
#     print(l)
#     #소수 판별기
#     for j in l:
#         a=int(j)
#         for i in range(2,a): #a숫자
#             if a%i==0:
#                 break
#             elif a!=1 and a%i!=0 and i==(a-1):
#                 print(i)
#                 sum+=1
#             # print(a

# print(sum)




