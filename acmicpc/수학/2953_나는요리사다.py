result = [0, 0]

for i in range(1,6):
    data = list(map(int, input().split()))
    total = sum(data)
    if result[0] < total:
        result[0] = total
        result[1] = i

print(result[1], result[0])