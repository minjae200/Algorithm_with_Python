import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == b: continue
    edges.append((c,a,b))
edges.sort()

def find_parent(parent, x):
    if x != parent[x]:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
