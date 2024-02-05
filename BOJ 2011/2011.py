password = [0]+list(input().strip())
n = len(password)
dp = [0 for _ in range(n)]
if password[1] != "0":
    dp[0] = dp[1] = 1

for i in range(2,n):
    if int(password[i]) > 0:
        dp[i] += dp[i-1]
    if 10 <= int(password[i-1]) * 10 + int(password[i]) <= 26:
        dp[i] += dp[i-2]
print(dp[n-1] % 1000000)