N,M = map(int,input().split())
K = list(map(int,input().split()))

arr = [0] * 11

for item in K:
    arr[K] += 1

result = 0
for i in range(1,M+1):
    N -= arr[i]
    result += arr[i] * N

print(result)