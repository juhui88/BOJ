import sys
input = sys.stdin.readline


n = int(input())

arr = [ input().strip() for _ in range(n)]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

