import sys
sys.setrecursionlimit(10**6)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

n,m,k = map(int,input().split())

graph = [[0 for a in range(m+1)] for b in range(n+1)]
visited = [[False for a in range(m+1)] for b in range(n+1)]

for _ in range(k):
    r,c = map(int,input().split())
    graph[r][c] = 1

cnt = 0
def in_range(y,x):
    return 0<=y<=n and 0<=x<=m

def DFS(a,b):
    global cnt
    visited[a][b] = True
    cnt += 1
    for i in range(4):
        y = dy[i] + a
        x = dx[i] + b
        if in_range(y,x) and visited[y][x] == False and graph[y][x] == 1:
            DFS(y,x)

arr=[]
def DFSALL():
    global cnt
    for i in range(n+1):
        for j in range(m+1):
            if graph[i][j] == 1 and visited[i][j] == False:
                cnt = 0
                DFS(i,j)
                arr.append(cnt)

DFSALL()
print(max(arr))