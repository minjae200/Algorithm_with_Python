from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
n, k = map(int, input().split())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

q = list()
for i in range(n):
    for j in range(n):
        if room[i][j] != 0:
            q.append((room[i][j], 0, i, j))

q.sort()
q = deque(q)

def bfs():
    global q
    global s
    while q:
        virus, time, x, y = q.popleft()
        if time == s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or 0 > ny or n <= nx or n <= ny:
                continue
            if room[nx][ny] != 0:
                continue
            room[nx][ny] = virus
            q.append((virus, time+1, nx, ny))

bfs()
print(room[x-1][y-1])

"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2

3 3
1 0 2
0 0 0
3 0 0
1 2 2
"""