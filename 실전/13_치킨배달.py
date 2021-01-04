n, m = map(int, input().split())

house = []
chicken = []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(len(data)):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

from itertools import combinations

candidates = list(combinations(chicken, m))

result = 1e9

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        result += temp
    return result

for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)