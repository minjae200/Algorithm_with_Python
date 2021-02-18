import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arrayA = [input().rstrip() for _ in range(n)]
arrayB = [input().rstrip() for _ in range(n)]

AtoB = [[x==y for x, y in zip(arow, brow)] for arow, brow in zip(arrayA, arrayB)]

def flip(i, j):
    for row in AtoB[i:i+3]:
        row[j:j+3] = [not val for val in row[j:j+3]]

ans = 0
for i in range(n-2):
    for j in range(m-2):
        if not AtoB[i][j]:
            flip(i,j)
            ans += 1
print(ans) if all(all(row) for row in AtoB) else print(-1)