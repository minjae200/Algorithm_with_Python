n = int(input())

array = []
for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

array = sorted(array, key=lambda person: person[1])

for person in array:
    print(person[0], end= ' ')