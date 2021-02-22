N = int(input())
array = list(map(int,input().split()))

array.sort()
num = 1
for i in range(N):
    if num < array[i]:
        break
    num += array[i]
print(num)