import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
array = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
result = deque()

for _ in range(m):
    a, b = map(int, input().split())
    array[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        result.append(i)

while result:
    data = result.popleft()
    for j in array[data]:
        indegree[j] -= 1
        if indegree[j] == 0:
            result.append(j)
    print(data, end=' ')