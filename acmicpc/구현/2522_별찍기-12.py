n = int(input())

array = []
for i in range(1, n+1):
    prefix = ' ' * (n-i)
    stars = '*' * (i)
    if i != n:
        array.append(prefix + stars)
    print(prefix+stars)
for i in reversed(array):
    print(i)