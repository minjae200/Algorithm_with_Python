import sys, copy
input = sys.stdin.readline

n, m = map(int, input().split())
cctv_list = []
office = []

for i in range(n):
    office.append(list(map(int, input().split())))
    for j in range(m):
        if office[i][j] != 0 and office[i][j] != 6:
            cctv_list.append([i, j, office[i][j]])

# 우 상 좌 하
dx = [0, 1, 0, -1, 0]
dy = [0, 0, -1, 0, 1]
direction = [
    [],
    [[1], [2], [3], [4]],                   # Camera No 1.
    [[1,3], [2,4]],                         # Camera No 2.
    [[1,2], [2,3], [3,4], [1,4]],           # Camera No 3.
    [[1,2,3], [2,3,4], [1,3,4], [1,2,4]],   # Camera No 4.
    [[1,2,3,4]]                             # Camera No 5.
]

def observe(arr, y, x, d):
    for i in d:
        ny, nx = y, x
        while True:
            ny, nx = ny + dy[i], nx + dx[i]
            if 0 > ny or n <= ny or 0 > nx or m <= nx: break
            if arr[ny][nx] == 6: break
            arr[ny][nx] = '#'

def dfs(office, cctv):
    global result
    temp = copy.deepcopy(office)
    if cctv == cctv_len:
        num = 0
        for i in range(n):
            num += temp[i].count(0)
        result = min(result, num)
        return
    y, x, kind = cctv_list[cctv]
    for i in direction[kind]:
        observe(temp, y, x, i)
        dfs(temp, cctv + 1)
        temp = copy.deepcopy(office)

cctv_len = len(cctv_list)
result = int(1e9)
dfs(office, 0)
print(result)