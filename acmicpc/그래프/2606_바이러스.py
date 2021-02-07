import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

computers = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

visited = [False] * (n+1)
result = -1
def dfs(virus):
    global result
    visited[virus] = True
    result += 1
    for i in computers[virus]:
        if visited[i]: continue
        dfs(i)
dfs(1)
print(result) if result != -1 else print(0)