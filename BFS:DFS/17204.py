import sys
input = sys.stdin.readline

n,k = map(int,input().split())
graph = [int(input()) for _ in range(n)]
visited = [False for _ in range(n)]

count = 0
index = 0
flag = True
while(True):
    count +=1
    if visited[index] : 
        flag = False
        break

    visited[index] = True
    
    if graph[index] == k:
        break

    index = graph[index]

if(flag): print(count)
else: print(-1)


