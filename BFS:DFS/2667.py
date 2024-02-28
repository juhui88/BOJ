import sys
input = sys.stdin.readline

n = int(input())

graph = [ list(map(int,input().strip())) for _ in range(n)]
visited = [ [False for _ in range(n)] for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

spaces = []
cnt = 0
def DFSall():
    global cnt
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and visited[i][j] == False:
                cnt = 0
                # print("첫방문 인덱스",i,j)
                DFS(i,j)
                spaces.append(cnt)
                
def DFS(a,b):
    global cnt
    visited[a][b] = True
    cnt += 1
    for i in range(4):
        x = dx[i] + a
        y = dy[i] + b
        if in_range(x,y) and graph[x][y] == 1 and visited[x][y] == False:
            # print("방문하고 있는 인덱스",x,y)
            # print('현 cnt', cnt)
            DFS(x,y)
DFSall()
print(len(spaces))
spaces.sort()
for i in spaces:
    print(i)