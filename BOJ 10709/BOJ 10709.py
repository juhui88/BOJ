import sys
from collections import deque
input = sys.stdin.readlines
sys.setrecursionlimit(10**6)

h,w = map(int,input().split())

JOI = [list(input().strip()) for _ in range(h)]


for i in range(h):
    q = deque()
    for j in range(w):
        q.append(JOI[i][j])
    cloud = 0
    wind = 0
    while(q):
        space = q.popleft()
        if space == "c":
            print(0,end=" ")
            cloud += 1
            wind = 0

        if space == ".":
            if cloud >=1:
                wind += 1
                print(wind,end=" ")
            else:
                print(-1,end=" ")
        
    print()

    