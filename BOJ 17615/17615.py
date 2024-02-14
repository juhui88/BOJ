import sys
input = sys.stdin.readline

n = int(input())
balls= list(input().strip())

blue_balls = balls.count("B")
red_balls = n - blue_balls

ans = min(blue_balls, red_balls)
cnt = 0
for i in range(n):
    if balls[i] != balls[0]: break
    cnt += 1

if balls[0] == "B":
    ans = min(ans, blue_balls-cnt)
else:
    ans = min(ans, red_balls-cnt)

cnt = 0
for i in range(n-1,-1,-1):
    if balls[i] != balls[n-1]: break
    cnt += 1

if balls[n-1] == "B":
    ans = min(ans, blue_balls-cnt)
else:
    ans = min(ans, red_balls-cnt)

print(ans)