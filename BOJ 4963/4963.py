import sys
sys.setrecursionlimit(10**6)

global graph, visited, cnt

dx = [1,0,-1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,1,-1]

land = []
def in_range(y,x , h, w):
    return 0<=y<h and 0<=x<w


arr = []
def DFSall(w,h):
    global graph, cnt , visited
    result_arr = []
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == False:
                cnt = 0
                DFS(i,j , w,h)
                
                result_arr.append(cnt)

    print(len(result_arr)) 
                         

def DFS(i,j, w, h):
    global cnt, visited, graph
    visited[i][j] = True
    cnt += 1
    for k in range(8):
        y = dy[k] + i
        x = dx[k] + j
        if in_range(y,x,h,w) and visited[y][x] == False and graph[y][x] == 1 :
            DFS(y, x, w, h)
            


while True:
    cnt = 0
    w,h = map(int,input().split())
    if (w==0 and h==0):
        break
    graph = []
    visited = [[False for a in range(w)] for b in range(h)]
    for i in range(h):
        arr = list(map(int,input().split()))
        graph.append(arr)
    
    DFSall(w,h)