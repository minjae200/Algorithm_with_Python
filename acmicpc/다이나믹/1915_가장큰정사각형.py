n, m = map(int, input().split())
array = [list(map(int, list(input()))) for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and array[i][j] == 1:
            array[i][j] += min(array[i-1][j], array[i][j-1], array[i-1][j-1])
        answer = max(answer, array[i][j])
print(answer**2)
