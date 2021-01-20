n = int(input())
t = [0]
p = [0]
for _ in range(n):
    duration, pay = map(int, input().split())
    t.append(duration)
    p.append(pay)
dp = [-1] * (n+1)

def solve(day):
    if day == n+1:
        return 0
    if day > n+1:
        return -1e9
    if dp[day] != -1:
        return dp[day]
    dp[day] = max(solve(day+1), solve(day+t[day]) + p[day])
    return dp[day]


ret = solve(1)
print(ret)