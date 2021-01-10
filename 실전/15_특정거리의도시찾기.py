from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
result = list()
while q:
    now = q.popleft()
    if distance[now] == k:
        result.append(now)
    for next_node in graph[now]:
        if distance[next_node] != -1:
            continue
        distance[next_node] = distance[now] + 1
        q.append(next_node)

if not result:
    print(-1)
else:
    result.sort()
    for i in range(len(result)):
        print(result[i])    