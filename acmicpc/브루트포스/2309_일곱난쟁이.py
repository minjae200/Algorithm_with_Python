from itertools import combinations

array = list(int(input()) for _ in range(9))

result = []
for combi in list(combinations(array, 7)):
    if sum(combi) == 100:
        result = list(combi)
result.sort()

for i in result:
    print(i)
