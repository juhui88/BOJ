import sys
input = sys.stdin.readline

R,C,M = map(int,input().split())

sharks = []
sea = [[0]*(C+1) for _ in range(R+1)]

sea[0][0] = (1) # 낚시왕의 초기 위치
for i in range(M):
    r,c,s,d,z= map(int,input().split())
    sea[r][c] = [[s,d,z]]
    sharks.append([r,c,s,d,z])

direction = [
    ["방향정보", "dy", "dx"],
    [-1,0], #위
    [1,0], #아래
    [0,1], # 오른쪽
    [1,0], # 왼쪽
]

def in_range(y,x):
    return 1<= y <=C and 1<=x<=R

def closest_fish(index):
    for i in range(C):
        if sea[i][index] !=0:
            fish_size = sea[i][index][0][2]
            sea[i][index] = 0
            return fish_size

def swim_shark():
    sea_copy = sea.copy()
    for i in range(1,C):
        for j in range(1,R):
            if sea_copy[i][j] != 0:
                temp = sea_copy[i][j][0]
                #속력, 이동방향, 크기
                print(temp)
                for _ in range(temp[0]):
                    y = i + direction[temp[1]][0]
                    x = j + direction[temp[1]][1]
                    if in_range(y,x):
                        if y == R or x == C:
                            if temp[1] == 1:
                                temp[1] = 2
                            elif temp[1] == 2:
                                temp[1] = 1
                            elif temp[1] == 3:
                                temp[1] = 4
                            else:
                                temp[1] = 3
                        
                        if sea_copy[y][x] == 0:
                            sea_copy[y][x] = temp
                sea_copy[i][j] = 0
                
                print(i,j,"에 있던거 여기로 옮김",y,x)
                        


time = 6
fishing_king_x = 0
fishing = 0
while (time >0):
    time -= 1
    fishing_king_x += 1

    fishing += closest_fish(fishing_king_x)
    swim_shark()




