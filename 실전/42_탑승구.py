G = int(input())
P = int(input())
air = [[] for _ in range(P+1)]

for i in range(1, P+1):
    data = int(input())
    for j in range(1, data+1):
        air[i].append(j)

visited = [False] * (G+1)
d = [0] * (P+1)

def dfs(index):
    for i in air[index]:
        if visited[i]: continue
        visited[i] = True
        if d[i] == 0 or dfs(d[i]):
            d[i] = index
            return True
    return False

result = 0
for i in range(1, P+1):
    visited = [False] * (G+1)
    if dfs(i): result += 1
    else: break
print(result)