import sys
import heapq
input = sys.stdin.readline
m, n = map(int, input().split())
array = [input() for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x, y):
    q = []
    heapq.heappush(q, (0, x, y))
    visited[x][y] = True
    while q:
        cnt, cur_x, cur_y = heapq.heappop(q)
        if cur_x == n-1 and cur_y == m-1:
            return cnt
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny]: continue
                heapq.heappush(q, (cnt + int(array[nx][ny]), nx, ny))
                visited[nx][ny] = True

visited = [[False] * m for _ in range(n)]
print(bfs(0, 0))
