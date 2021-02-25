import heapq
import sys
input = sys.stdin.readline
n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

INF = sys.maxsize

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

one = dijkstra(1)
d1 = dijkstra(v1)
d2 = dijkstra(v2)
result = min(one[v1] + d1[v2] + d2[n], one[v2] + d2[v1] + d1[n])
print(result if result < INF else -1)