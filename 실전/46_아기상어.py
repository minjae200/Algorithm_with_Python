from collections import deque

n = int(input())
board = []

shark = {
    'x': 0,
    'y': 0,
    'size': 2
}

for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            shark['x'], shark['y'] = i, j

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    dist = [[-1] * n for _ in range(n)]
    q = deque([(shark['x'], shark['y'])])
    dist[shark['x']][shark['y']] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or 0 > ny or n <= nx or n <= ny:
                continue
            if shark['size'] < board[nx][ny]:
                continue
            if dist[nx][ny] != -1:
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
    return dist

def find(dist):
    x, y = 0, 0
    min_dist = int(1e9)
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= board[i][j] and board[i][j] < shark['size']:
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    x, y = i, j
    if min_dist == int(1e9):
        return None
    else:
        return x, y, min_dist

result = 0
ate = 0

while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        shark['x'], shark['y'] = value[0], value[1]
        result += value[2]
        board[shark['x']][shark['y']] = 0
        ate += 1
        if ate >= shark['size']:
            shark['size'] += 1
            ate = 0