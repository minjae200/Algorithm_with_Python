import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

island = 0

def BFS(y, x):
    visited[y][x] = True
    q = deque()
    q.append((y, x))
    array[y][x] = island
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and array[ny][nx] != 0:
                    array[ny][nx] = island
                    visited[ny][nx] = True
                    q.append((ny, nx))

for i in range(n):
    for j in range(n):
        if not visited[i][j] and array[i][j] != 0:
            island += 1
            BFS(i, j)

ans = int(1e9)

def solve(index):
    dist = [[-1] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if array[i][j] == index:
                q.append((i, j))
                dist[i][j] = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n: continue
            if array[ny][nx] != 0 and array[ny][nx] != index:
                return dist[y][x]
            if array[ny][nx] == 0 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))

for i in range(1, island+1):
    ans = min(ans, solve(i))
print(ans)