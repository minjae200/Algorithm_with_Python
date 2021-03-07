"""
Timeout .....

g = int(input())
p = int(input())
array = [int(input()) for _ in range(p)]

docking = [0] * (p+1)
ans = 0

def matching(plane):
    for i in range(1, array[plane-1]+1):
        if visited[i]: continue
        visited[i] = True
        if (docking[i] == 0 or matching(docking[i])):
            docking[i] = plane
            return True
    return False

for i in range(1, p+1):
    visited = [False] * (g+1)
    if (matching(i)): ans += 1
    else: break
print(ans)
"""

import sys
input = sys.stdin.readline

g = int(input())
p = int(input())
plane = [int(input()) for _ in range(p)]

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

parent = {i : i for i in range(g+1)}
ans = 0
for i in plane:
    x = find_parent(parent, i)
    if x == 0:
        break
    union_parent(parent, x, x-1)
    ans += 1
print(ans)