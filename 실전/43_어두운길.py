import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bridges = []

total = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    bridges.append((c, a, b))
    total += c

bridges.sort()
parent = [0] * (n)

for i in range(n):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

result = 0
for bridge in bridges:
    cost, a, b = bridge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(total-result)
"""
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
"""