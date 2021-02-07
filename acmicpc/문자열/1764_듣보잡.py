import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array1 = set()
array2 = set()
for _ in range(n):
    array1.add(input().split('\n')[0])
for _ in range(m):
    array2.add(input().split('\n')[0])

result = array1 & array2
print(len(result))
for i in sorted(result): print(i)
