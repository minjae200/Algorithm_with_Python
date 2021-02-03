A, B = map(int, input().split())
C = int(input())

minute = B+C
hour = minute // 60
result = ((hour + A) % 24, minute % 60)

print(result[0], result[1])