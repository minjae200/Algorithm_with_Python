import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)
dist = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
print(graph)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = []
dist[1] = 0
heapq.heappush(q, (0, 1))

while q:
    distance, cur = heapq.heappop(q)
    if dist[cur] < distance:
        continue
    for i in graph[cur]:
        next_distance = distance + 1
        if next_distance < dist[i]:
            dist[i] = next_distance
            heapq.heappush(q, (dist[i], i))

position, distance = 0, 0
for i in range(1, n+1):
    if dist[i] == INF:
        continue
    if distance < dist[i]:
        distance = dist[i]
        position = i
print(position, distance, len(list(filter(lambda x: x==distance, dist))))
