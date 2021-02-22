from itertools import permutations
n = int(input())
data = list(map(int, input().split()))

result = -1e9
for permutation in list(permutations(data, n)):
    temp = 0
    for i in range(1, len(permutation)):
        temp += abs(permutation[i-1]-permutation[i])
    result = max(result, temp)
print(result)
