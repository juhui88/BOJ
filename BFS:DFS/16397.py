import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,t,g = map(int,input().split())

visited = [False for _ in range(100000)]
visited[n] = True

cnt = 0

def in_range(n):
    if 0 < n < 100000:
        return True
    else:
        return False

def BFS():
    queue = deque([[n,0]])
      
    while (queue) :
        v, cnt = queue.popleft()
        if cnt > t:
            return "ANG"
        
        if v == g:
            return cnt
                 
        if in_range(v+1) and visited[v+1] == False:
            visited[v+1] = True
            queue.append([v+1, cnt +1])

        if in_range(v*2):
            k  = v *2
            strk = str(k)
            strk = str(int(strk[0]) - 1) + strk[1:] 
            k = int(strk)
            if visited[k] == False:
                visited[k] = True
                queue.append([k, cnt + 1])
    
    return "ANG"

result = BFS()
print(result)