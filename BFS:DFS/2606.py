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



def DFS(G,index):

    visited[index] = True
    
    for w in G:
        if visited[w] == False:
            DFS(graph[w],w)



DFS(graph[1],1)

print(visited.count(True) -1)