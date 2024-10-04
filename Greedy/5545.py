import sys,math
input = sys.stdin.readline

n = int(input()) # 토핑 종류
a,b = map(int,input().split()) # 도우 가격, 토핑 가격
c = int(input()) # 도우 열량

D =[int(input()) for _ in range(n)]
D.sort(reverse=-1)

money = a
kcal = c

best_pizza = c/a

for i in range(n):
    new_money = money + b
    new_kcal = kcal + D[i]

    new_best_pizza = new_kcal/new_money

    if best_pizza < new_best_pizza:
        money = new_money
        kcal = new_kcal
        best_pizza = new_best_pizza
    else:
       break

print(math.trunc(best_pizza))

