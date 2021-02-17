n, m = input().split()

helmet = list(map(int, input().split()))
vest = list(map(int, input().split()))

scores = list()
for i in range(int(n)):  # 가능한 조합 다 만들기
    for j in range(int(m)):
        scores.append(helmet[i] + vest[j])

max = 0
for i in range(len(scores)):  # 가장 큰 방어력 구하기
    if(scores[i] > max):
        max = scores[i]

print(max)
