n, c = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

end = array[-1] - array[0]
start = 1e9
for i in range(n-1):
    start = min(start, array[i+1]-array[i])
result = 0

while (start <= end):
    value = array[0]
    count = 1
    mid = (start + end) // 2
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)
