import sys
input = sys.stdin.readline

S,C = map(int,input().split())
L = [ int(input()) for _ in range(S)]
L = sorted(L)

def binary_search(target, start, end):
    total = 0
    mid = (start + end) // 2
    if start > end: # start가 더 커지면 반환
        return mid 

    for item in L: # 현재 mid 값으로 파가 몇개로 잘릴 수 있는 지 계산
        total += (item // mid)

    if total < target:
        return binary_search(target, start, mid -1)
    else:
        return binary_search(target, mid + 1, end)
length = binary_search(C, 1,max(L)) # 가장 큰 값과 1 사이에 중간 값으로 계산했을때 C만큼 나오는지 함수로 계속 확인
print(sum(L) - length * C)