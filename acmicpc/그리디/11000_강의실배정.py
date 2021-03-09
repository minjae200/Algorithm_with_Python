import heapq
import sys

input = sys.stdin.readline

n = int(input())

timeTable = [list(map(int, input().split())) for _ in range(n)]
timeTable.sort(key=lambda x: x[0])

queue = []
heapq.heappush(queue, timeTable[0][1])

for i in range(1, n):
    if queue and queue[0] <= timeTable[i][0]:
        heapq.heappop(queue)
    heapq.heappush(queue, timeTable[i][1])
# print(queue)
print(len(queue))