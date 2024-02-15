import sys
input = sys.stdin.readline

n = int(input())
P = list(map(int,input().split()))
m = int(input())

dp = [-float("inf") for _ in range(m+1)]
for i in range(n-1,-1,-1):
    p = P[i]
    for j in range(p, m+1):
        dp[j] = max(dp[j], i, dp[j-p]*10 + i)
print(dp[m])


# for i in range(1,m+1):
#     w = 0
#     print(i, "번째")
#     if dp[i-1] != -1:
#         arr = list(map(int,str(dp[i-1]).strip()))
#         for a in arr:
#             w += P[a]

#     for k in range(n-1, -1,-1):
#         if i >= w + P[k] :
#             if dp[i-1] == -1:
#                 dp[i] = k
#             else:
#                 arr = [k] + arr
#                 arr = sorted(arr, reverse=False)
#                 print("arr", arr)
#                 num = ""
#                 for item in arr:
#                     num += str(item)
                
#                 dp[i] = max(dp[i],int(num), dp[i-1])
                
#         if i >= P[k]:
#             if dp[i-1] == -1:
#                 dp[i] = k
#             else:
                
                
#                 dp[i] = max(dp[i],k, dp[i-1])
#         print(dp)

# for i in range(1,m+1):
#     if dp[i-1] != -1:
#         arr = list(dp[i-1].strip())
#         for item in arr:
#             room += P[item]
#     이전 값 방 번호의 가격 계산하기
    
#     room_price = 0
#     room_num = []
#     index = n-1

#     while(index >= 0):
#         if i >= room_price + P[index]:
#             room_price += P[index]
#             room_num.append(str(index))
#             room_num = sorted(room_num, reverse=False)
#         else:
#             index -= 1
            