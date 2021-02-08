from collections import deque

f, s, g, u, d = map(int, input().split())
INF = int(10e9)
dp = [INF] * (f + 1)

def bfs(pos):
    q = deque()
    q.append(pos)
    dp[pos] = 0

    while q:
        cur = q.popleft()
        u_cur = cur + u
        if u_cur > f: u_cur = cur
        d_cur = cur - d
        if d_cur < 1: d_cur = cur

        if dp[u_cur] == INF:
            q.append(u_cur)
            dp[u_cur] = min(dp[u_cur], dp[cur] + 1)
        if dp[d_cur] == INF:
            q.append(d_cur)
            dp[d_cur] = min(dp[d_cur], dp[cur] + 1)
bfs(s)
print(dp[g]) if dp[g] != INF else print("use the stairs")