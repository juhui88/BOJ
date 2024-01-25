import sys
input = sys.stdin.readline

r,c,n =map(int,input().split())
board = [list(input().strip()) for _ in range(r)]

def install_bomb(second):
    for i in range(r):
        for j in range(c):
            if board[i][j] == ".":
                board[i][j] = second + 3
            # 2초 후에 있는 일 (모든 칸에 폭탄 설치)
            # 0은 초기에 있던 폭탄 위치가 아님을 표시해줌

dy = [1,0,-1,0]
dx = [0,1,0,-1]

    

def in_range(y,x):
    return 0<= y < r and 0<= x < c


for second in range(2, n+1):  #3초일때부터 시작
    if second % 2 == 0: # 짝수초일때 설치
        install_bomb(second)
    
    else: # 홀수 초 일때 폭발
        for i in range(r):
            for j in range(c):
                if board[i][j] == "O": # 초기 폭탄 터지는 경우
                    board[i][j] = "."
                    for k in range(4):
                        y = i + dy[k]
                        x = j + dx[k]
                        if in_range(y,x) and board[y][x] !="O":
                            board[y][x] = "."

                if board[i][j] == second: # 후에 있는 폭탄이 3초 뒤에 터지는 경우
                    board[i][j] = "."
                    for k in range(4):
                        y = i + dy[k]
                        x = j + dx[k]
                        if in_range(y,x) and board[y][x] != second:
                            board[y][x] = "."
    
    



for i in range(r):
    for j in range(c):
        if type(board[i][j]) == int:
            print("O",end="")
        else:
            print(board[i][j], end="")
        
    print()
