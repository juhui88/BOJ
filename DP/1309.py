import sys
input = sys.stdin.readline

N = int(input())

dp = [[1,1,1] for _ in range(N+1)]

for i in range(2,N+1):
    for j in range(3):
        if j == 0:
            dp[i][j] = sum(dp[i-1]) % 9901
        elif j==1 :
            dp[i][j] =(dp[i-1][j-1] + dp[i-1][j+1] ) % 9901
        else:
            dp[i][j] = (dp[i-1][j-2] + dp[i-1][j-1]) % 9901

print(sum(dp[-1]) % 9901)