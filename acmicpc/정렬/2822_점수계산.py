array = [(int(input()), i) for i in range(1,9)]
array = sorted(array, reverse=True)[:5]
result = 0
index = []
for data, i in array:
    result += data
    index.append(i)
print(result)
print(*sorted(index))