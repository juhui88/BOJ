import sys
input = sys.stdin.readline

N = list(map(int,input().strip()))

length = len(N) // 2

if sum(N[:length]) == sum(N[length:]):
    print("LUCKY")
else:
    print("READY")