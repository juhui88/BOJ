import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int,input().split())))
M = int(input())
M_list = list(map(int,input().split()))

def binary_search(target, start, end):
    if start > end: # 범위를 넘어도 못찾는다면 -1을 반환
        return False
    
    mid = (start + end) // 2
    if mid >= N : return False

    if target < A[mid] : end = mid - 1
    elif target == A[mid]: return True
    else: start = mid + 1

    return binary_search(target, start, end)

for item in M_list:
    if binary_search(item, 0, N):
        print(1)
    else:
        print(0)
    