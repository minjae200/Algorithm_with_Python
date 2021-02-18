import sys
input = sys.stdin.readline

n = int(input())
array = [input().split()[0] for _ in range(n)]
alpha = [0] * 26
for data in array:
    for i, cur in enumerate(data[::-1]):
        alpha[ord(cur) - ord('A')] += pow(10, i)
alpha.sort(reverse=True)
result = 0
for i in range(9, 0, -1):
    result += i * alpha[9-i]
print(result)