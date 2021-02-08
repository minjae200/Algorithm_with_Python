import sys
import heapq
input = sys.stdin.readline
v, e = map(int, input().split())
edges = []
parent = [-1] * (v+1)
for i in range(1, v+1):
    parent[i] = i

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

for _ in range(e):
    a, b, c = map(int, input().split())
    # edges.append((c,a,b))
    heapq.heappush(edges, (c,a,b))
# edges.sort()
result = 0
# for edge in edges:
while edges:
    cost, a, b = heapq.heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)