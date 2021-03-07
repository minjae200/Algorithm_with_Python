import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

dr = [-2, -2, 0, 0, +2, +2]
dc = [-1, 1, -2, 2, -1, 1]

from collections import deque

def BFS(r, c):
    q = deque()
    visited = [[False] * n for _ in range(n)]
    q.append((r, c, 0))
    visited[r][c] = True

    while q:
        cr, cc, cd = q.popleft()
        if (r2, c2) == (cr, cc):
            return cd
        for i in range(len(dr)):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if visited[nr][nc]: continue
                visited[nr][nc] = True
                q.append((nr, nc, cd+1))
    return -1

print(BFS(r1, c1))