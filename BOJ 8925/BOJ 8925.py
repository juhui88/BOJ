T = int(input())

for i in range(T):
    n, L = map(int, input().split())
    arr = input()
    num = n - L + 1
    score = list()
    l = L
    y = 0
    while num > 0:
        x = 0
        for j in range(y, l):
            if arr[j] == '1':
                x += 1
        score.append(x)
        y += 1
        l += 1
        num -= 1
    max = 0
    for k in range(len(score)):
        if score[k] > max:
            max = score[k]
            index = k
    print("{0} {1}".format(index + 1, index + L))
