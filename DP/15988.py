import sys
input = sys.stdin.readline

T = int(input())
dp = [0]
dp.append(1)
dp.append(2)
dp.append(4)

for _ in range(T):
    n = int(input())
    if n <= 3:
        print(dp[n])
    else:
        for i in range(len(dp), n+1):
            dp.append((dp[i-1] + dp[i-2] + dp[i-3])%1000000009)

        print(dp[n])

