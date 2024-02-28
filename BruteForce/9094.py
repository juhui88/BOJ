def isPossible(n,m):
    cnt = 0
    for i in range(1,n):
        for j in range(i+1,n):
            x = (i**2 + j**2 + m)/(i*j)
            if x.is_integer():
                cnt +=1
    return cnt
T = int(input())

for i in range(T):
    a,b= map(int,input().split())
    print(isPossible(a,b))
