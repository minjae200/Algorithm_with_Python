array = list(map(int, input().split()))

dice = [0] * 7

for i in range(3):
    dice[array[i]] += 1

max_ = 0
index = 0
for i in range(1, 7):
    if dice[i] >= max_:
        max_ = dice[i]
        index = i
result = 0
if max_ == 3:
    result = 10000 + index * 1000
elif max_ == 2:
    result = 1000 + index * 100
else:
    result = index * 100

print(result)