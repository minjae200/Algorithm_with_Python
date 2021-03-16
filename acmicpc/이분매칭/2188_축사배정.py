import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = [[] for i in range(n+1)]
d = [0 for i in range(m+1)]

def dfs(start):
    if visited[start] == True:
        return False
    visited[start] = True
    for i in s[start]:
        if d[i] == False or dfs(d[i]):
            d[i] = start
            return True
    return False

for i in range(1, n+1):
    a = list(map(int, input().split()))
    for j in a[1:]:
        s[i].append(j)
for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    dfs(i)
print(len(d) - d.count(0))