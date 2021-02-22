from itertools import permutations

n = int(input())
array = [i for i in range(1, n+1)]

results = list(permutations(array, n))
for result in results:
    print(*result)
