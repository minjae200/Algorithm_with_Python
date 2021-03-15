import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()
start = 1
end = trees[-1]

while start <= end:
    mid = (start + end) // 2
    bring = 0
    # index = find_tree(mid)
    index = bisect_left(trees, mid)
    bring = sum(trees[index:]) - mid * (len(trees[index:]))
    if bring >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)