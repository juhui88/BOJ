n = int(input())

for i in range(n):
    arr = input()
    tmp = 0
    score = 0
    for j in range(len(arr)):
        if arr[j] == 'O':
            tmp += 1
            score += tmp
        else:
            tmp = 0

    print(score, end='\n')
