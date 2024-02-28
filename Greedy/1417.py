import sys
input = sys.stdin.readline

n = int(input())
vote = [int(input()) for _ in range(n)]

def is_elected():
    dasom_vote = vote[0]
    for i in range(1,n):
        if dasom_vote <= vote[i]:
            return False
    return True

def max_index():
    maxI = 0
    for i in range(1,n):
        if vote[maxI] < vote[i]:
            maxI = i
    return maxI

cnt = 0
flag = True
if n == 1:
    print(0)
else:
    while(flag):
        while(is_elected() == False):
            maxI = max_index()
            if maxI == 0:
                maxI += 1
            vote[0] += 1
            vote[maxI] -= 1
            cnt += 1
        flag = False
        print(cnt)

