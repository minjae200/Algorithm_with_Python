string = str(input())
result = 0

result = int(string[0])
for num in string[1:]:
    num = int(num)
    if result == 0:
        result += num
    else:
        result *= num

print(result)