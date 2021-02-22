n, m = map(int, input().split())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))
print(*sorted(arrayA+arrayB))