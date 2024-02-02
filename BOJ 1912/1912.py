import sys
input = sys.stdin.readline

n = int(input())
lst =[float("-inf")] + list(map(int,input().split()))

dp = [lst[0]]

for i in range(1,n+1):
    dp.append(max(dp[i-1] + lst[i], lst[i]))

print(max(dp))