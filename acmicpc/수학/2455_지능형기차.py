
train = 0
result = 0
for _ in range(4):
    a, b = map(int, input().split())
    train = train - a + b
    result = max(result, train)

print(result)
