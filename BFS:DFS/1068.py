import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

root_node_num =0
for i in range(n):
    if arr[i] == -1: # 루트 노드 찾기
        root_node_num = i
remove_node_num = int(input())

if(remove_node_num == root_node_num): # 삭제하는 노드가 루트노드라면 0반환 후 종료
    print(0)
    exit()

graph = [[] for _ in range(n)] # i번째의 노드의 자식 노드 담는 그래프
is_del_list = [False for _ in range(n)] # 삭제되었는지 여부 저장

for i in range(n):
    if arr[i] != -1: 
        graph[arr[i]].append(i)


remove_que = deque([remove_node_num])
is_del_list[remove_node_num] = True

# while(remove_que):
#     v = remove_que.popleft()
#     for num in graph[v]:



while(remove_que): # 삭제되어야할 노드 찾기
    v = remove_que.popleft()
    for num in graph[v]:
        if not is_del_list[num]:
            remove_que.append(num)
            is_del_list[num] = True

if(is_del_list.count(False) == 1): # 남은 노드가 하나라면 1반환 후 종료
    print(1)
    exit()

for i in range(n):
    if is_del_list[i]:
        while(len(graph[i]) != 0):
            graph[i].pop()
    else:
        if remove_node_num in graph[i]:
            graph[i].remove(remove_node_num)

visited = [False for _ in range(n)]
count = 0
q = deque([root_node_num])
while(q):
    v = q.popleft()
    for num in graph[v]:
        if not visited[num] and not is_del_list[num]:
            visited[v] = True
            q.append(num)
            if len(graph[num]) == 0:
                count += 1

            

print(count)