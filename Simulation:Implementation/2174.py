import sys
input = sys.stdin.readline
from collections import deque

a,b = map(int,input().split())
n,m = map(int,input().split())

ground = [[0]*(a+1) for _ in range(b+1)]

dirs = [
    ["E",0,1],
    ["S", -1,0],
    ["W",0,-1],
    ["N", 1,0]
    # 인덱스 커지면 오른쪽으로 도는거
    # 작아지면 왼쪽으로 도는거
]

def find_now_dir(dir):
    for i in range(4):
        if dirs[i][0] == dir:
            return dirs[i], i
        
def fint_robot(robot_num):
    for i in range(b+1):
        for j in range(a+1):
            if ground[i][j] !=0 and ground[i][j][0] == robot_num:
                return ground[i][j]

for i in range(n):
    x,y, direction = map(str,input().split())
    x = int(x)
    y = int(y)
    ground[y][x] = [i+1,y,x,direction]
    # 로봇숫자, y좌표, x좌표, 방향정보

#print(ground)
commands = deque()
for _ in range(m):
    robot_num, c, rep = map(str,input().split())
    robot_num = int(robot_num)
    rep = int(rep)
    commands.append([robot_num, c, rep])

def in_range(y,x):
    return 1<= y <b+1 and 1<=x< a+1

flag = True
#print(commands)
while(commands and flag):
    command = commands.popleft() # 로봇숫자, 명령종류, 반복횟수 리스트 
    robot = fint_robot(command[0]) # 로봇숫자, y좌표, x좌표, 방향정보
    now_dir, index = find_now_dir(robot[3]) # 현재 바라보는 곳
    now_y = robot[1]
    now_x = robot[2]

    for _ in range(command[2]): # 반복횟수만큼
        if command[1] == "L":
            if index == 0:
                index = 3
            else: 
                index -= 1
        
            
        if command[1] == "R":
            if index == 3:
                index = 0
            else: 
                index += 1

        ground[now_y][now_x][3] = dirs[index][0]
        
        if command[1] == "F":
            y = now_y + now_dir[1]
            x = now_x + now_dir[2]
            if in_range(y,x):
                if ground[y][x] != 0: # 다른 로봇이랑 부딪힘
                    print(f"Robot {robot[0]} crashes into robot {ground[y][x][0]}")
                    flag = False
                    break
                else: # 다른 로봇이랑 안 부딪힘
                    ground[now_y][now_x] = 0
                    now_y = y
                    now_x = x
                    ground[y][x] = [robot[0], y,x, now_dir[0]]

            else:

                print(f"Robot {robot[0]} crashes into the wall")
                flag = False
                break
            
if flag:
    print("OK")
