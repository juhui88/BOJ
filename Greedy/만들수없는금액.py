N = int(input())
coins = list(map(int,input().split()))

coins = sorted(coins)

money = 1
for item in coins:
    if item < money:
        break
    else:
        money += item
print(money)