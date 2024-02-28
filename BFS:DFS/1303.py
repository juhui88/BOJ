import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
for _ in range(m):
    arr = list(input().strip())
    new_arr = []
    for item in arr:
        if item == "W":
            new_arr.append(1)
        else:
            new_arr.append(0)
    graph.append(new_arr)

visited = [[False for _ in range(n)] for _ in range(m)]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

w_soldier = []
b_soldier = []

cnt = 0

def in_range(x,y):
    return 0<=x<m and 0<=y< n

def DFSall():
    global cnt 
    for i in range(m):
        for j in range(n):
            if visited[i][j] == False:
                cnt = 0
                flag = graph[i][j]
                DFS(i,j,flag)
                if flag == 1:
                    w_soldier.append(cnt**2)
                else : 
                    b_soldier.append(cnt **2)
            
def DFS(a,b, flag):
    global cnt
    visited[a][b] = True
    cnt += 1
    for i in range(4):
        x = dx[i] + a
        y = dy[i] + b
        if in_range(x,y) :
            if flag == graph[x][y] and visited[x][y] == False:
                DFS(x,y,flag)
            

DFSall()
print(sum(w_soldier), sum(b_soldier))