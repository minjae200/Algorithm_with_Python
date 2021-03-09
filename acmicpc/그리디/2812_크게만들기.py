import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(input().strip())

tk = k
t = []
for i in range(n):
    while tk > 0 and t and t[-1] < s[i]:
        del t[-1]
        tk -= 1
    t.append(s[i])
print(''.join(t[:n-k]))