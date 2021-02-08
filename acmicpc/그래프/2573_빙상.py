from collections import deque
import copy
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    global visited
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    icies = []
    while queue:
        cur_x, cur_y = queue.popleft()
        ice = 0
        for i in range(4):
            nx, ny = cur_x + dx[i], cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny]: continue
                if array[nx][ny] == 0:
                    ice += 1
                else:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
        icies.append((cur_x, cur_y, ice))
    return icies

def meltSnow(x, y):
    global array
    temp = copy.deepcopy(array) 
    for i in range(n):
        for j in range(m):
            if array[i][j] > 0:
                sea = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < n and 0 <= nj < m:
                        if array[ni][nj] == 0:
                            sea += 1
                temp[i][j] -= sea
    array = temp

result = 0
while True:
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    icies = []
    for i in range(n):
        for j in range(m):
            if visited[i][j]: continue
            if array[i][j] > 0:
                cnt += 1
                icies += bfs(i, j)
    if cnt >= 2:
        print(result)
        break
    if not icies:
        print(0)
        break
    # 얼음 녹이기
    # meltSnow(i, j)
    for ice in icies:
        x, y, h = ice
        array[x][y] = max(0, array[x][y]-h)
    result += 1