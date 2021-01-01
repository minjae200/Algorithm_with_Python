#https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3

import heapq

def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    length = len(food_times)
    previous = 0
    while length * (q[0][0]-previous) <= k:
        k -= (length * (q[0][0]-previous))
        previous = q[0][0]
        heapq.heappop(q)
        length -= 1
    result = sorted(q, key = lambda x : x[1])
    return result[k % length][1]

foods = [8, 6, 4]
k = 15

print(solution(foods, k))