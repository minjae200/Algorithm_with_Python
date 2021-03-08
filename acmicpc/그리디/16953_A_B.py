import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())

def bfs(a, b):
    q = deque()
    q.append((a, 1))
    while q:
        cur, cnt = q.popleft()
        if cur == b:
            return cnt
        if (2*cur) <= b:
            q.append((2*cur, cnt+1))
        if int(str(cur) + '1') <= b:
            q.append((int(str(cur) + '1'), cnt+1))
    return -1

print(bfs(a,b))