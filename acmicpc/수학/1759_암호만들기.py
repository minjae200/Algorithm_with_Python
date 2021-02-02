from itertools import combinations

L, C = map(int, input().split())
array = sorted(list(map(str, input().split())))

results = list(combinations(array, L))
# results = list(map(lambda x: ''.join(x), list(combinations(array, L))))

vowels = ['a', 'e', 'i', 'o', 'u']

for result in results:
    count = 0
    for word in result:
        if word in vowels:
            count += 1

    if (count >= 1) and (L-count >= 2):
        print(''.join(result))