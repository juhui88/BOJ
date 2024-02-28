import sys
input = sys.stdin.readline
from collections import deque

sentence =["!"]+list(input().strip())
N = int(input())
words = [list(input().strip()) for _ in range(N)]
dp = [[float("inf")]*(len(sentence)) for _ in range(len(sentence))]
dp[0][0] = 0

def cost(word1, word2):
    return sum( word1[i] != word2[i] for i in range(len(word1)))
    
for i in range(1,len(sentence)+1):
    if (dp[i-1][0] != float("inf")):
        for word in words:
            l = len(word)
            word1 = sentence[i:i+l]
            if (sorted(word1) ==sorted( word)):
                c = cost(word1, word)
                dp[i][i+l-1] = min(dp[i][i+l-1], dp[i-1][0] + c)
                dp[i+l-1][0] = min(dp[i+l-1][0], dp[i][i+l-1])

if (dp[-1][0]==float("inf")): print(-1)
else: print(dp[-1][0])
