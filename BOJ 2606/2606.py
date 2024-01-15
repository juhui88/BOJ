import sys
input = sys.stdin.readline

n = int(input())
link = int(input())

graph = [[]for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(link):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


cnt = 0

def DFS(G,index):
    global cnt
    cnt += 1
    visited[index] = True
    print(cnt, visited, index , G)
    for w in G:
        if visited[w] == False:
            DFS(graph[w],w)
    cnt -= 1


DFS(graph[1],1)

print(cnt)