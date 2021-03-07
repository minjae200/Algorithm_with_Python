r, c = map(int, input().split())
array = [list(input()) for _ in range(r)]

dr = [-1, 0, 1]
dc = [1, 1, 1]
ans = 0
visited = [[False] * c for _ in range(r)]
def connect(y, x):
    if x == c-1:
        return True
    
    visited[y][x] = True
    for d in range(3):
        nr = y + dr[d]
        nc = x + dc[d]
        if 0 <= nr < r and 0 <= nc < c and array[nr][nc] == '.' and not visited[nr][nc]:
            if connect(nr, nc):
                return True
    return False

for i in range(r):
    if array[i][0] == '.':
        if connect(i, 0):
            ans += 1
print(ans)