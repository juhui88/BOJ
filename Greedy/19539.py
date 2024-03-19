import sys
input = sys.stdin.readline

N = int(input())
trees = list(map(int,input().split()))

if sum(trees)%3 == 0:
    one_n = 0
    two_n = 0
    for item in trees:
        two_n += item // 2
        one_n += item % 2
    if one_n == two_n: print("Yes")
    elif one_n < two_n:
        two_n -= one_n
        if two_n % 3 == 0: print("YES")
        else: print("NO")
    else: print("NO") 
else:
    print("NO")