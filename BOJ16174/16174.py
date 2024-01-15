import sys
input = sys.stdin.readline

n = int(input())

k = 0
board = [ [] for _ in range(n)]
for i in range(n):
    arr = list(map(int,input().split()))
    for a in arr:
        set = (k,a)
        board[i].append(set)
        k += 1

visited = [False for _ in range(n*n)]

graph = [[] for _ in range(n*n)]

k = 0
for i in range(n):
    for j in range(n):
        num = board[i][j][1]
        if i + num < n:
            graph[k].append(board[i+num][j])

        if j + num < n:
            graph[k].append(board[i][j+num])

        k+=1

flag = False
def DFS(G,v):
    global flag
    visited[v] = True
    for w in G:
        if w[1] == -1:
            flag = True
            return
    
    for w in G:
        if visited[w[0]] == False:
            DFS(graph[w[0]],w[0])

DFS(graph[0],0)

if (flag) :
    print("HaruHaru")
else:
    print("Hing")