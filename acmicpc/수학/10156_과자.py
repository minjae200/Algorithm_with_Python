k, n, m = map(int, input().split())

result = k * n - m
print(0) if result <= 0 else print(result)