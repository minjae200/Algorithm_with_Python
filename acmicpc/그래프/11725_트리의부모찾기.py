import sys
sys.setrecursionlimit(10**5)
n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

result = [0 for _ in range(n+1)]

def dfs(root):
    for child in tree[root]:
        if result[child] == 0:
            result[child] = root
            dfs(child)

dfs(1)
for i in range(2, n+1):
    print(result[i])