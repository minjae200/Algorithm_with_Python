from bisect import bisect_left
import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
m = int(input())
find_array = list(map(int, input().split()))
array.sort()

for data in find_array:
    start = 0
    end = n - 1
    find = False
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == data:
            find = True
            break
        if array[mid] > data:
            end = mid - 1
        else:
            start = mid + 1
    print(1 if find else 0)