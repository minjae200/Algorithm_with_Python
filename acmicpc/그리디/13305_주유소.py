n = int(input())
dist = list(map(int, input().split()))
dist.append(0)
cost = list(map(int, input().split()))
array = list(zip(cost, dist))

import sys
cur_cost = sys.maxsize
result = 0
for i in range(n):
    if cur_cost > cost[i]:
        cur_cost = cost[i]
    result += cur_cost * dist[i]

print(result)