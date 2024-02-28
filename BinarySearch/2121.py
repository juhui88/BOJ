import sys
input = sys.stdin.readline

N = int(input())
A,B = map(int,input().split())
coor = [list(map(int,input().split())) for _ in range(N)]
coor = sorted(coor)

def binary_search(target, start, end):
    if start > end: # 못 찾으면 실패
        return False
    
    mid = (start + end) // 2
   
    if target[0] == coor[mid][0] and target[1] == coor[mid][1]:
        return True
    
    if coor[mid] > target: end = mid -1
    else :start = mid + 1

    return binary_search(target, start, end)

ans = 0
for i in range(N):
    x,y = coor[i][0], coor[i][1]
    start = 0
    end = N-1
    if binary_search([x+A,y],start,end) and binary_search([x,y+B],start,end) and binary_search([x+A,y+B],start,end):
        ans += 1
print(ans)