import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

babyShark = 2
eat_fish = 0

current = (0,0)
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            current = (i,j)

dx = [0,-1,0,1]
dy = [-1,0,1,0]

def in_range(y,x):
    return 0<=y<n and 0<=x<n

def bfs(current):
    dist = [[0]*n for _ in range(n)]
    visited = [ [False]*n for _ in range(n)]

    q = deque([current])
    visited[current[0]][current[1]] = True
    list = []

    while q:
        now_y, now_x = q.popleft()

        for i in range(4):
            y = dy[i] + now_y
            x = dx[i] + now_x
            if in_range(y,x) and visited[y][x] == False:
                fish = graph[y][x]
                if babyShark >= fish:
                    # 물고기의 크기가 아기상어보다 작거나 같다면
                    q.append((y,x))
                    visited[y][x] = True
                    dist[y][x] = dist[now_y][now_x] + 1 # 일단 방문
                    
                    # 물고기가 더 작긴한데 0이 아니라면 먹을 수 있음
                    if babyShark > fish and graph[y][x] != 0:
                        list.append((y,x,dist[y][x]))
    
    # 제일 가까운 것, 제일 위에 있는것, 제일 왼쪽에 있는것 순으로 정렬 뒤에서 pop을 해줄거라서 맨 뒤에 있는기준으로 해주어야 함
    return sorted(list, key=lambda x: (-x[2], -x[0], -x[1]))


eat_fish = 0
result = 0
while True:
    can_bite_fish = bfs(current)
    # 리스트들 반납

    # 더 이상 먹을 수 있는게 없으면 break
    if len(can_bite_fish) == 0:
        break

    y,x,distance = can_bite_fish.pop()
    result += distance
    graph[y][x] = 0
    eat_fish += 1

    # 현재 위치 갱신
    current = (y,x)
    if eat_fish == babyShark:
        eat_fish=0
        babyShark += 1
print(result)
