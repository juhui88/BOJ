import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())
dy = [0,1,0,-1]
dx = [1,0,-1, 0]

def in_range(y,x, n,m):
    return 0 <= y < n and 0 <= x < m

def DFS(i,j):
    visited[i][j] = True

    for k in range(4):
        y = i + dy[k]
        x = j + dx[k]
        if in_range(y,x,N,M) and visited[y][x] == False and graph[y][x] == 1:
            DFS(y,x)


for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0]*M for _ in range(N)]
    visited= [[False]*M for _ in range(N)]
    for _ in range(K):
        a,b = map(int,input().split())
        graph[b][a] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == False:
                cnt += 1
                DFS(i,j)

    print(cnt)




