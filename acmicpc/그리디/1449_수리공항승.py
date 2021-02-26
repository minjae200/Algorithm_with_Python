n, l = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

answer = 1
start = array[0]
end = array[0] + l
for i in range(n):
    if start <= array[i] < end:
        continue
    else:
        start = array[i]
        end = array[i] + l
        answer += 1
print(answer)