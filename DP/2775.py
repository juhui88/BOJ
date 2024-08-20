import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    K = int(input())
    N = int(input())

    DP = [[0 for _ in range(N+1)] for _ in range(K+1)]
    DP[0] = [_ for _ in range(N+1)]


    for i in range(1,K+1):
        for j in range(1,N+1):
            DP[i][j] = DP[i][j-1] + DP[i-1][j]
            
    print(DP[K][N])