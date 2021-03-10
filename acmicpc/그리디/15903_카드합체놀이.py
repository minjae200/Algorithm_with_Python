import heapq

n, m = map(int, input().split())
array = list(map(int, input().split()))
heapq.heapify(array)

for i in range(m):
    num1 = heapq.heappop(array)
    num2 = heapq.heappop(array)
    heapq.heappush(array, num1+num2)
    heapq.heappush(array, num1+num2)

print(sum(array))