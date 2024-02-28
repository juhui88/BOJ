import sys
input = sys.stdin.readline

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

G = [[] for _ in range(n*n)]
for i in range(n*n):
    

print(G)
visited = [False for _ in range(n)]

def bfs(index):
    visited[index] = True
