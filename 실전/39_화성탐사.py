import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

for _ in range(int(input())):
    n = int(input())
    dist = [[INF] * n for _ in range(n)]
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    

    q = []
    dist[0][0] = graph[0][0]
    heapq.heappush(q, (dist[0][0], 0, 0))

    while q:
        distance, x, y = heapq.heappop(q)
        if dist[x][y] < distance:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or 0 > ny or n <= nx or n <= ny:
                continue
            next_distance = distance + graph[nx][ny]
            if dist[nx][ny] > next_distance:
                dist[nx][ny] = next_distance    
                heapq.heappush(q, (next_distance, nx, ny))

        
    print(dist[n-1][n-1])