t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort()
    result = 0
    for i in range(2, n):
        result = max(result, array[i]-array[i-2])
    print(result)