array = []

for _ in range(7):
    array.append(int(input()))

array = list(filter(lambda x: (x%2 == 1), array))
if array:
    print(sum(array))
    print(min(array))
else:
    print(-1)