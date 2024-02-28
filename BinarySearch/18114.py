import sys
input = sys.stdin.readline

N,C = map(int,input().split())
W = sorted(list(map(int,input().split())))

def binary_search(target ,start, end):
    if start > end: return False 
    
    mid = (start + end) // 2
    
    if W[mid] == target: return True
    elif W[mid] > target: end = mid - 1
    else: start = mid + 1

    return binary_search(target, start, end)

flag = False
if binary_search(C,0,N-1):
    flag = True

if not flag :
    i = 0
    j = N-1
    while (i < j):
        sumW = W[i] + W[j]
        if W[i] + W[j] == C:
            flag = True
            break

        elif sumW > C:
           j -= 1
        else:
            if C-sumW != W[i] and C-sumW != W[j]  and binary_search(C-sumW,0, N-1):
                flag = True
                break
            i += 1

if flag: print(1)
else: print(0)

