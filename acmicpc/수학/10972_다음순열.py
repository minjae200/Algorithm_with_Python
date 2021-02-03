"""
from itertools import permutations

n = int(input())
array = tuple(map(str, input().split()))

result = sorted(list(permutations(array, n)))
try:
    print(' '.join(list(result[result.index(array)+1])))
except:
    print(-1)
"""

n = int(input())
array = list(map(int, input().split()))

find = False

for i in range(n-1, 0, -1):
    if array[i] > array[i-1]:
        for j in range(n-1, 0, -1):
            if array[i-1] < array[j]:
                array[i-1], array[j] = array[j], array[i-1]
                array = array[:i] + sorted(array[i:])
                find = True
                break
    if find:
        # print(*array)
        print(' '.join(map(str, array)))
        break
if not find:
    print(-1)