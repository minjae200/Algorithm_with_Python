string = str(input())
result = []
sum = 0
for i in range(len(string)):
    if string[i].isdigit():
        sum += int(string[i])
    else:
        result.append(string[i])

result.sort(key=lambda x: ord(x))
print(''.join(result) + str(sum))