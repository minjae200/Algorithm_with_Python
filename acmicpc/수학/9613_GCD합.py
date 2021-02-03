from itertools import combinations
import math

for _ in range(int(input())):
    data = list(map(int, input().split()))
    n = data[0]
    array = data[1:]
    total = 0
    for part in list(combinations(array, 2)):
        total += math.gcd(part[0], part[1])
    print(total)