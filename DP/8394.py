import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(10000001)]

dp[0] = 1
dp[1] = 1

for i in range(2,n + 1):
    dp[i] = (dp[i-2] + dp[i-1]) % 10
    # dp[i] = dp[i-2] + dp[i-1]

# ans = str(dp[n])
# print(ans[-1])
# 원래는 이렇게 했다가 메모리 초과가 떠서 나머지를 반환하는 식으로 바꿔줌

print(dp[n])