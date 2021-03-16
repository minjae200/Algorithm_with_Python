import sys
input = sys.stdin.readline
n = int(input())
mount = list(map(int, input().split()))

maxMount = 0
cnt = 0
result = 0
for mnt in mount:
    if mnt > maxMount:
        maxMount = mnt
        cnt = 0
    else:
        cnt += 1
    result = max(result, cnt)
print(result)