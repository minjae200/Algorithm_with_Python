n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

temp = [[0] * m for _ in range(n)]
result = 0

def get_safe_area():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    return count

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 > nx or 0 > ny or m <= ny or n <= nx:
            continue
        if temp[nx][ny] == 0:
            temp[nx][ny] = 2
            virus(nx, ny)

def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = board[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_safe_area())
        return
    for i in range(n):
        for j in range(m): 
            if board[i][j] == 0:
                board[i][j] = 1
                count += 1
                dfs(count)
                board[i][j] = 0
                count -= 1

dfs(0)
print(result)