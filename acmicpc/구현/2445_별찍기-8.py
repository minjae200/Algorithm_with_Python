n = int(input())
array = []

for i in range(1, n+1):
    data = '*'*i + ' '*(n-i)
    array.append(data)

for data in reversed(array[:-1]):
    array.append(data)

for i in array:
    print(i+i[::-1])