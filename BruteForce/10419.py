def lateMaxM(d):
    maxM = 0
    for t in range(d):
        s = t**2
        if t + s <= d:
            maxM = t
        else:
            return maxM
    return maxM

T = int(input())

for i in range(T):
    d = int(input())
    print(lateMaxM(d))

