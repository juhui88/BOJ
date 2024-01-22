import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m,k,x = map(int,input().split())

graph = [[] for b in range(n+1)]
visited = [False for b in range(n+1)]
way = [-1 for b in range(n+1)]
way[x] = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

for i in graph[x]:
    if i == x:
        way[i] = 0
    else:
        way[i] = 1

def BFS():
    q = deque()
    q.append([x,0])
    visited[x] = True
    
    while q:
        now, cnt = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                q.append([i,cnt+1])
                visited[i] = True
                way[i] = cnt + 1

BFS()

flag = False
for i in range(len(way)):
    if way[i] == k:
        print(i)
        flag = True

if not flag:
    print(-1)



# def DFS(a):
#     global cnt
#     cnt += 1
#     visited[a] = True

#     for i in graph[a]:  
#         if visited[i] == False :
#             way[i] = min(way[i], cnt)
#             DFS(i)     

#     cnt -=1

# DFS(x)
# flag = False
# print(way)
# for w in range(len(way)):
#     if way[w] == k:
#         print(w)
#         flag = True

# if not flag:
#     print(-1)