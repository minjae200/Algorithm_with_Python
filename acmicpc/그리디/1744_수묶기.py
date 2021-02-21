N = int(input())
array = [int(input()) for _ in range(N)]

positive = sorted(list(filter(lambda x: x > 0 and x != 1, array)), reverse=True)
negative = sorted(list(filter(lambda x: x <= 0, array)))
one = len(list(filter(lambda x: x==1, array)))

result = one

for i in range(0, len(positive)-1, 2):
    result += positive[i] * positive[i+1]
if len(positive) % 2 == 1:
    result += positive[-1]

for i in range(0, len(negative)-1, 2):
    result += negative[i] * negative[i+1]
if len(negative) % 2 == 1:
    result += negative[-1]

print(result)