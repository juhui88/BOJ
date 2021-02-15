n, m = input().split()

helmet = list(map(int, input().split()))
vest = list(map(int, input().split()))

scores = list()
for i in range(int(n)):
    for j in range(int(m)):
        scores.append(helmet[i] + vest[j])

max = 0
for i in range(len(scores)):
    if(scores[i] > max):
        max = scores[i]

print(max)
