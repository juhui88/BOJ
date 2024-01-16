import sys
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [ input().strip() for _ in range(n)]
visited = [[False * n] for _ in range(n)]

dx = [0, 1]
dy = [1, 0]

w_soldier=[]
b_soldier = []
# W이면 flag = True, B이면 flag = False
def DFS(x,y, flag):
    isW = graph[x][y] == "W"

    if (flag == isW):
        