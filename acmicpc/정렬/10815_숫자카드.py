import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
m = int(input())
data = list(map(int, input().split()))

array.sort()

for num in data:
    start = 0
    end = len(array)-1
    find = False
    while start <= end:
        mid = (start + end) // 2
        if num == array[mid]:
            find = True
            break
        else:
            if array[mid] < num:
                start = mid + 1
            else:
                end = mid -1
    print(1 if find else 0, end=' ' )