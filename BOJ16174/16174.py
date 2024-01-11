n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

print(board)
print(visited)

# 항상 아래를 먼저 가는걸로

space = board[0][0]

for i in range()