import sys
input = sys.stdin.readline

N, L = map(int,input().split())
leak = sorted(list(map(int,input().split())))

sticker = 1

i = 0
while (i < N -1):
    for j in range(i+1, N):
        if leak[j] - leak[i] + 1 <= L: # 스티커 하나로 될 때
            continue
        else:
            sticker += 1
            break
    i = j
print(sticker)