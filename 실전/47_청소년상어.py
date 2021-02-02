array = [[-1] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [data[j*2], data[j*2+1] - 1]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

import copy
result = 0

def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None

def move_fishes(array, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(array, i)
        if position is None:
            continue
        x, y = position[0], position[1]
        direction = array[x][y][1]
        for _ in range(8):
            nx, ny = x + dx[direction], y + dy[direction]
            if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                if not (nx == now_x and ny == now_y):
                    array[x][y][1] = direction
                    array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                    break
            direction = (direction + 1) % 8

def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    for _ in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4:
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)

    # 잡아먹기
    total += array[now_x][now_y][0]
    array[now_x][now_y][0] = -1

    # 물고기 이동
    move_fishes(array, now_x, now_y)

    possible_positions = get_possible_positions(array, now_x, now_y)
    # 계속 진행
    if len(possible_positions) == 0:
        result = max(result, total)
        return
    for next_x, next_y in possible_positions:
        dfs(array, next_x, next_y, total)
    
dfs(array, 0, 0, 0)
print(result)