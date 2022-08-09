from sys import stdin
input = lambda:stdin.readline().rstrip()

L = []
for _ in range(int(input())):
    L.append(input())

L = set(L)

if len(L)<=3:
    print('valid')
else:
    print('invalid')


