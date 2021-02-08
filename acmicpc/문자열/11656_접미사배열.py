data = input()
array = []
for i in range(len(data)):
    array.append(data[i:])
array.sort()
for i in array:
    print(i)