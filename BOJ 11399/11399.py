import sys
input = sys.stdin.readline

n = int(input())
withdraw = sorted(list(map(int,input().split())))

total = 0
for i in range(n):
    for j in range(n-i):
        total += withdraw[j]

print(total)