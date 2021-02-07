# 북 동 남
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
n, m = map(int, input().split())
r, c, d = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

def turn(d):
    if d == 0: return 3
    else: return d-1

clean = 0
cnt = 0
while True:

    if cnt == 4:
        br, bc = r - dr[d], c - dc[d]
        if array[br][bc] != 1:
            r, c, cnt = br, bc, 0
        else:
            break

    if array[r][c] == 0:
        array[r][c] = -1
        clean += 1

    nd = turn(d)
    nr, nc = r + dr[nd], c + dc[nd]
    if array[nr][nc] == 0:
        r, c, d, cnt = nr, nc, nd, 0
    else:
        d, cnt = nd, cnt + 1
print(clean)