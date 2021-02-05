array = []
for _ in range(8):
    array.append(input())

result = 0
for i in range(8):
    if i % 2 == 0:
        flag = 0
    else:
        flag = 1
    for j in range(flag, 8, 2):
        if array[i][j] == 'F':
            result += 1
print(result)