import sys
input = sys.stdin.readline

n = int(input())
p1, p2 = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

num = -1

def DFS(G,v):
    global cnt, num
    visited[v] = True
    cnt += 1
    if p2 in G:
        num = cnt
        return
    
    for w in G:
        if visited[w] == False:
            DFS(graph[w],w)
    
    cnt -= 1
     
cnt = 0
DFS(graph[p1], p1)
print(num)