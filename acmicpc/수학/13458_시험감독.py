N = int(input())
array = list(map(int, input().split()))
B, C = map(int, input().split())

array = list(filter(lambda x: x > 0,[x-B for x in array]))
result = N

for i in array:
    if i % C != 0:
        result += 1
    result += (i // C)
print(result)