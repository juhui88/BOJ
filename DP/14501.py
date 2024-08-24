import sys, math
input = sys.stdin.readline

n = int(input())
TP = [ list(map(int,input().split())) for _ in range(n)]
dp = [0] * (n+1)
for i in range(n):
    t,p = TP[i][0],TP[i][1]
    if t + i > n:
        continue
    
    dp[i] = max(dp[:i+1])
    dp[i+t] = max(dp[i]+p,dp[i+t] )

print(max(dp))