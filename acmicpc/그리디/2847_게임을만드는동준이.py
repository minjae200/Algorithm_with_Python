n = int(input())
array = [int(input()) for _ in range(n)]
answer = 0
for i in range(n-1, 0, -1):
    if array[i] <= array[i-1]:
        decrease = (array[i]-(array[i-1]+1))
        array[i-1] += decrease
        answer += abs(decrease)
print(answer)