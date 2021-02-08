import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(parent):
    global visited
    global adj
    visited[parent] = True
    for child in adj[parent]:
        if visited[child]: continue
        dfs(child)

for _ in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    adj = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        adj[i].append(array[i-1])
    visited = [False] * (n+1)
    result = 0
    for i in range(1, n+1):
        if visited[i] == False:
            dfs(i)
            result += 1
    print(result)