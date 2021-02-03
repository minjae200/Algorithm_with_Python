import math

n, k = map(int, input().split())
array = [True for i in range(n+1)]

count = 0
result = 0
for i in range(2, n+1):
    if array[i]:
        j = 1
        while i*j <= n:
            if array[i*j]:
                # print(i*j, end=' ')
                array[i*j] = False
                count +=1
                if count == k:
                    result = i*j
                    break
            j += 1
    if count == k:
        break
print(result)
