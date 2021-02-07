import sys
sys.setrecursionlimit(10**6)
n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

result = [0 for _ in range(n+1)]

def dfs(root, tree1, result1):
    for child in tree1[root]:
        if result1[child] == 0:
            result1[child] = root
            dfs(child, tree1, result1)

dfs(1, tree, result)
for i in range(2, n+1):
    print(result[i])