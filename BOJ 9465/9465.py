import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    sticker = [list(map(int,input().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    if n!= 1:
        dp[0][1] = sticker[0][1] + dp[1][0]
        dp[1][1] = sticker[1][1] + dp[0][0]
        for j in range(2,n):
            dp[0][j] = max(dp[1][j-1]+ sticker[0][j], dp[1][j-2] + sticker[0][j] )
            dp[1][j] = max(dp[0][j-2] + sticker[1][j], dp[0][j-1] + sticker[1][j])
    print(max(dp[0][n-1], dp[1][n-1]))
    

