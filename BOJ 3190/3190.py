import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]
graph[1][1] = 1

for _ in range(k):
    y,x = map(int,input().split())
    graph[y][x] = "a"
    
l = int(input())
q = deque()
for _ in range(l):
    x, c = input().split()
    x = int(x)
    q.append([x,c])


dy = [0,1,0,-1]
dx = [1,0,-1,0]
# 인덱스 커지면 오른쪽으로 돌고 인덱스 작아지면 왼쪽으로 돔

def in_range(y,x):
    return 1<=y<n+1 and 1<=x<n+1

flag = True
time = 0
now_dir = 0
head_y ,head_x ,tail_y ,tail_x = 1,1,1,1
snake_len = 1
snake_pass_by = deque([[head_y,head_x]])
while(flag):
    if len(q) != 0:
        direction = q.popleft()
    else:
        direction = [0,0]

    while(time != direction[0]):
        time += 1
        head_y += dy[now_dir]
        head_x += dx[now_dir]

        if in_range(head_y, head_x) and graph[head_y][head_x] != 1:

            snake_pass_by.append([head_y,head_x])

            if graph[head_y][head_x] == "a": # 사과 있을 때
                snake_len += 1

            else: #사과 없을 때
                pass_by = snake_pass_by.popleft()
                tail_y = pass_by[0]
                tail_x = pass_by[1]
                graph[tail_y][tail_x] = 0
            
            graph[head_y][head_x] = 1

        else:
            flag = False
            print(time)
            break
    
    if direction[1] == "L":
        if now_dir == 0:
            now_dir = 3
        else:
            now_dir -= 1
    else:
        if now_dir == 3:
            now_dir = 0
        else:
            now_dir += 1
    
