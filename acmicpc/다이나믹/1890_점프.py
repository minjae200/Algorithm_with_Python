n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n) for _ in range(n)]

dp[0][0] = 1

for y in range(n):
    for x in range(n):
        if array[y][x] == 0:
            break
        ny = y + array[y][x]
        nx = x + array[y][x]
        if 0 <= nx < n:
            dp[y][nx] += dp[y][x]
        if 0 <= ny < n:
            dp[ny][x] += dp[y][x]
print(dp[-1][-1])