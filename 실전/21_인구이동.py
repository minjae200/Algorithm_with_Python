from collections import deque

N, L, R = map(int, input().split())
kingdom = []
for _ in range(N):
    kingdom.append(list(map(int, input().split())))
result = 0
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(x, y, index):
    q = deque()
    q.append((x,y))
    visited[x][y] = index
    uniteds = []
    total = 0
    while q:
        x, y = q.popleft()
        uniteds.append((x,y))
        total += kingdom[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or 0 > ny or N <= nx or N <= ny:
                continue
            if visited[nx][ny] != -1:
                continue
            if L <= abs(kingdom[x][y] - kingdom[nx][ny]) <= R:
                visited[nx][ny] = index
                q.append((nx, ny))

    people = total // len(uniteds)
    for united in uniteds:
        x, y = united
        kingdom[x][y] = people
    

while True:
    visited = [[-1] * N for _ in range(N)]
    group = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                bfs(i, j, group)
                group += 1
    if group == N * N:
        break
    result += 1
print(result)

"""
2 20 50
50 30
20 40

2 40 50
50 30
20 40

2 20 50
50 30
30 40

3 5 10
10 15 20
20 30 25
40 22 10

4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
"""