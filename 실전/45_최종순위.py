
from collections import deque

def topology_sort():
    result = []
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break
        now = q.popleft()
        result.append(now)
        for i in range(1, n+1):
            if graph[i][now]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in reversed(result):
            print(i, end=' ')
        print()

for tc in range(int(input())):
    n = int(input())
    rank = list(map(int, input().split()))
    graph = [[False] * (n+1) for i in range(n+1)]
    indegree = [0] * (n+1)

    for i in range(n):
        for j in range(i+1, n):
            graph[rank[i]][rank[j]] = True
            indegree[rank[i]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[b][a] = True
            graph[a][b] = False
            indegree[a] -= 1
            indegree[b] += 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] += 1
            indegree[b] -= 1
    topology_sort()


