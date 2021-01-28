n = int(input())

planet_x, planet_y, planet_z =[], [], []
for i in range(n):
    x, y, z = map(int, input().split())
    planet_x.append((x, i))
    planet_y.append((y, i))
    planet_z.append((z, i))

planet_x.sort()
planet_y.sort()
planet_z.sort()

parent = [0] * (n)
for i in range(n):
    parent[i] = i

def find_parent(parent, x):
    if x != parent[x]:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if y > x:
        parent[y] = x
    else:
        parent[x] = y

edges = []
for i in range(1, n):
    edges.append((planet_x[i][0]-planet_x[i-1][0], planet_x[i][1], planet_x[i-1][1]))
    edges.append((planet_y[i][0]-planet_y[i-1][0], planet_y[i][1], planet_y[i-1][1]))
    edges.append((planet_z[i][0]-planet_z[i-1][0], planet_z[i][1], planet_z[i-1][1]))

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)
print(result)