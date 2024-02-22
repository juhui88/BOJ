import sys
input = sys.stdin.readline
from collections import deque


R,C,M = map(int,input().split())

sharks = deque()
for _ in range(M):
    sharks.append(list(map(int,input().split())))
    # 위치, 속력, 이동방향, 크기

fishing_king_x = 0

direction = [
    ["방향정보", "dy", "dx"],
    [1,-1,0], #위
    [2,1,0], #아래
    [3,0,1], # 오른쪽
    [4,0,-1], # 왼쪽
]

def in_range(y,x):
    return 1<=y<=R and 1<=x<=C


all_sharks_size = 0

for _ in range(C):
    fishing_king_x += 1
    same_col_sharks = []
    for s in range(len(sharks)):
        shark = sharks.popleft()
        if shark[1] == fishing_king_x:
            same_col_sharks.append(shark)
        else:
            sharks.append(shark)

    if len(same_col_sharks) > 0:
        same_col_sharks = sorted(same_col_sharks,key=lambda x: x[0] )
        all_sharks_size += same_col_sharks[0][4]
        # print("낚시왕이 잡았음 우하하", same_col_sharks[0])
        same_col_sharks = same_col_sharks[1:]

    for shark in same_col_sharks:
        sharks.append(shark)

# ---------------------(낚시왕 이동 후 가까운 상어 잡기)위코드
    # print("낚시왕한테 잡힌 후", sharks)   
    for shark in sharks:
        for _ in range(shark[2]):
            y = shark[0] + direction[shark[3]][1]
            x = shark[1] + direction[shark[3]][2]
            if in_range(y,x):
                shark[0] = y
                shark[1] = x
            else:
                if shark[3] == 1: shark[3] = 2
                elif shark[3] == 2: shark[3] = 1   
                elif shark[3] == 3: shark[3] = 4
                elif shark[3] == 4: shark[3] = 3

                shark[0] = shark[0] + direction[shark[3]][1]
                shark[1] = shark[1] + direction[shark[3]][2]

            
# --------------------- 상어 이동 위코드
    # print("상어 이동 완료", sharks)
    temp_shark = []
    for i in range(len(sharks)-1):
        # print("이전임 비교해봅시다",sharks)
        shark = sharks.popleft()
        
        # print("비교군1", shark)
        for j in range(len(sharks)):
            other_shark = sharks.popleft()
            # print("비교군2", other_shark)
            if shark[0] == other_shark[0] and shark[1] == other_shark[1]:
                if shark[4] < other_shark[4]:
                    shark = other_shark 
            else:
                sharks.append(other_shark) # 같은 좌표 아니면 다시 넣어줌
        
        # print("비교완료 하였습니다",sharks)
        temp_shark.append(shark)
        # print("이건 이제 같은 좌표에서 제일 큰 애임",temp_shark)


    for shark in temp_shark:
        sharks.append(shark)





print(all_sharks_size)



