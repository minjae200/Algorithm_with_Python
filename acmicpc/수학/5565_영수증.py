total = int(input())

array = []
for _ in range(9):
    array.append(int(input()))

print(total - sum(array))