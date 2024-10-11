import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
points = list(map(int, input().split()))
points.sort()

distance = []
for i in range(1,n):
    distance.append(points[i]-points[i-1])

distance.sort()

distance_sum = 0
for i in range(n-k):
    distance_sum += distance[i]

print(distance_sum)