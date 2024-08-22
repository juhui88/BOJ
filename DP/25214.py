import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))

dp = [0] *(n)
min_n = A[0]

print(dp[0], end=" ")
for i in range(1,n):
    if min_n > A[i]:
        min_n = A[i]
    dp[i] = max(dp[i-1], A[i] - min_n)
    print(dp[i], end=" ")


