import sys
from collections import deque
#input = sys.stdin.readlines
#sys.setrecursionlimit(10**6)

def can_print(queue, document):
    # 출력 조건
    # doc의 중요도가 queue에 있는 모든 문서의 중요도 보다 커야함
    for item in queue:
        if document[1] < item[1]: 
            return False
    return True


t = int(input())

for _ in range(t):
    n,m= map(int,input().split())
    importance = list(map(int,input().split()))
    q = deque()
    for i in range(n):
        q.append((i,importance[i]))
    cnt = 0
    
    while(q):
        doc = q.popleft()
        
        if(can_print(q,doc)):
            cnt += 1
            if doc[0] == m:
                break
        else:
            q.append(doc)
    print(cnt)

    