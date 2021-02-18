import sys
from collections import deque
input = sys.stdin.readline
l, w = map(int, input().split())
array = [input() for _ in range(l)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j):
    q = deque()
    visited = [[-1] * w for _ in range(l)]
    q.append((i,j))
    visited[i][j] = 0
    num = 0
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < l and 0 <= ny < w:
                if array[nx][ny] =='L' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[cx][cy] + 1
                    num = max(num, visited[nx][ny])
                    q.append((nx, ny))
    return num
result = 0
for i in range(l):
    for j in range(w):
        if array[i][j] == 'L':
            result = max(result, bfs(i, j))
print(result)