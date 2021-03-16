from collections import deque
import sys
input = sys.stdin.readline

MAX_V = 52
INF = int(1e9)

n = int(input())
capacity = [[0] * MAX_V for _ in range(MAX_V)]
flow = [[0] * MAX_V for _ in range(MAX_V)]
adj = [[] for _ in range(MAX_V)]


def CtoI(target):
    if target.isupper():
        return ord(target) - ord('A')
    else:
        return ord(target) - ord('a') + 26

def bfs(source, sink, visit):
    dq = deque()
    dq.append(source)

    while dq and visit[sink] == -1:
        sv = dq.popleft()
        for dv in adj[sv]:
            if capacity[sv][dv] - flow[sv][dv] > 0 and visit[dv] == -1:
                dq.append(dv)
                visit[dv] = sv
                if dv == sink:
                    break
    if visit[sink] == -1:
        return True
    else:
        return False

def edmondkarp(source, sink):
    total = 0

    while True:
        visit = [-1] * MAX_V
        if bfs(source, sink, visit):
            break
        minFlow = INF

        i = sink
        while i != source:
            minFlow = min(minFlow, capacity[visit[i]][i] - flow[visit[i]][i])
            i = visit[i]
        i = sink
        while i != source:
            flow[visit[i]][i] += minFlow
            flow[i][visit[i]] -= minFlow
            i = visit[i]
        total += minFlow
    return total

for _ in range(n):
    s, d, c = input().split()

    s = CtoI(s)
    d = CtoI(d)

    capacity[s][d] += int(c)
    capacity[d][s] += int(c)
    adj[s].append(d)
    adj[d].append(s)

source = CtoI('A')
sink = CtoI('Z')

print(edmondkarp(source, sink))