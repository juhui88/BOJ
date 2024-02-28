import sys
from collections import deque
input = sys.stdin.readline
N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i] = sorted(graph[i])

def DFS(v):
    visited[v] = True
    print(v, end =" ")

    for item in graph[v]:
        if visited[item] == False:
            DFS(item)


        
def BFS(v):
    queue = deque([v])
    visited[v] = True

    while(queue):
        v = queue.popleft()
        print(v, end =" ")
        for item in graph[v]:
            if visited[item] == False:
                queue.append(item)
                visited[item] = True

DFS(V)
visited = [False for _ in range(N+1)]
print()
BFS(V)