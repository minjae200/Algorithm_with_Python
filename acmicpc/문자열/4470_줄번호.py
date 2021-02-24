n = int(input())
array = list(input() for _ in range(n))

for i in range(1, n+1):
    print(str(i) + '. ' + array[i-1])
