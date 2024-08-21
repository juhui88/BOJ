import sys
input = sys.stdin.readline

N = int(input())
trees = list(map(int,input().split()))

sum_trees = sum(trees)
if sum_trees % 3 != 0:
    print("NO")
else:
    cnt = 0
    for i in trees:
        cnt += i // 2

    if cnt >= (sum_trees // 3):
        print("YES")
    else:
        print("NO")