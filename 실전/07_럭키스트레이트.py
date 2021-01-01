n = str(input())
length = len(n)
mid = len(n) // 2
right, left = n[:mid], n[mid:]
right_sum = 0
left_sum = 0

for i in range(len(right)):
    right_sum += int(right[i])
    left_sum += int(left[i])

print('LUCKY') if right_sum == left_sum else print('READY')