import sys
input = sys.stdin.readline

n = int(input())

lost = [0] + list(map(int,input().split()))
get =[0] + list(map(int,input().split()))

lost_get = [[0,0]]
dp = [[0]*101 for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1,101):
        if lost[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-lost[i]] + get[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])
