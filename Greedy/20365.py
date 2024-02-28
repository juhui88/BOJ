import sys
input = sys.stdin.readline

n = int(input())
colors = list(input().strip())

blue = 0
red = 0
flag = colors[0]

if flag == "B":
    blue += 1
else:
    red += 1

for i in range(1,n):
    if colors[i] == "B" and flag != colors[i]:
        blue += 1

    if colors[i] == "R" and flag != colors[i]:
        red += 1

    flag = colors[i] 

print(1+min(blue,red))