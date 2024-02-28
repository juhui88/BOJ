import sys
input = sys.stdin.readline

n,m,l,k = map(int,input().split())

coordinate = []
for _ in range(k):
    coor = list(map(int,input().split()))
    coordinate.append(coor)

result = []

for a in range(k):
    for b in range(k):
        stars = 0
        for i in range(k):
            if coordinate[a][0] <= coordinate[i][0] <= coordinate[a][0] + l and coordinate[b][1] <= coordinate[i][1] <= coordinate[b][1]+l:
                # 이 과정에서 기준이 되는 별 두개도 더해짐
                stars += 1 
        result.append(k-stars)
print(min(result))