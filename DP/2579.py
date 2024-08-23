import sys
input = sys.stdin.readline

n = int(input())
steps = [int(input()) for _ in range(n)]

dp = [0]*n

dp[0] = steps[0]
if n == 1:
    print(dp[0])
    exit()

dp[1] = steps[0]+steps[1]
if n == 2:
    print(dp[1])
    exit()

dp[2] = max(steps[1]+steps[2],dp[0] +steps[2])
if n == 3:
    print(dp[2])
    exit()


for i in range(3,n):   
    two_steps_once = dp[i-2] + steps[i]
    one_steps_twice = dp[i-3] + steps[i-1] + steps[i]
    if i > 3:
        two_stesp_twice = dp[i-4] + steps[i-2] + steps[i]
        dp[i] = max(two_steps_once,one_steps_twice,two_stesp_twice)
    else:
        dp[i] = max(two_steps_once, one_steps_twice)
    
print(dp[-1])