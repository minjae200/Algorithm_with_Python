n = int(input())
dp = [0] * 46
dp[1] = dp[2] = 1

def solve(num):
    if num <= 2:
        return 1
    if dp[num] != 0:
        return dp[num]
    dp[num] = solve(num-1) + solve(num-2)
    return dp[num]

print(solve(n))
