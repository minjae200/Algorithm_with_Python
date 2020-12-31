n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
index = 0
while True:
    index += data[index]
    if index >= len(data):
        break
    result += 1
print(result)