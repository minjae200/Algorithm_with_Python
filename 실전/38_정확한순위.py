n, m = map(int, input().split())
INF = int(1e9)
students = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(n):
    a, b = map(int, input().split())
    students[a][b] = 1

for i in range(1, n+1):
    students[i][i] = 0


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            students[i][j] = min(students[i][j], students[i][k] + students[k][j])

result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if students[i][j] != INF or students[j][i] != INF:
            count +=1
    if count == n:
        result +=1

print(result)
"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""