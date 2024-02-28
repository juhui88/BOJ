import sys
input = sys.stdin.readline

R,C = map(int,input().split())
cave = [list(input().strip()) for _ in range(R)]
N = int(input())
sticks = list(map(int,input().split()))

visited = [[False]*C for _ in range(R)]

dy = [1,0,-1,0]
dx = [0,1,0,-1]



for i in range(N):
    if i % 2 == 0: # 짝수이면 왼쪽에서 오른쪽으로
        for j in range(C):
            if cave[R-sticks[i]][j] == "x":
                cave[R-sticks[i]][j] == "."
                for k in range(1,4):
                    if cave[R-sticks[i] + dy[k]][j + dx[k]] == "x":
                        
                

    else: # 홀수이면 오른쪽에서 왼쪽으로
        for j in range(C-1,-1,-1):
            if cave[R-sticks[i]][j] == "x":