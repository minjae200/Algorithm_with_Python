from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)

from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)