data = [0]
for _ in range(4):
    data.append(input())
k = int(input())
rotate = [list(map(int, input().split())) for _ in range(k)]
import copy
for i in range(k):
    select, direction = rotate[i]
    
    temp = copy.deepcopy(data)
    right_direction = direction
    if direction == 1:
        temp[select] = temp[select][-1] + temp[select][:-1]
    else:
        temp[select] = temp[select][1:]+ temp[select][:1]

    for j in range(select, 4):
        if data[j][2] == data[j+1][6]:
            break
        if right_direction == -1:
            temp[j+1] = temp[j+1][-1] + temp[j+1][:-1]
            right_direction = 1
        else:
            temp[j+1] = temp[j+1][1:] + temp[j+1][:1]
            right_direction = -1

    left_direction = direction
    for j in range(select, 1, -1):
        if data[j][6] == data[j-1][2]:
            break
        if left_direction == -1:
            temp[j-1] = temp[j-1][-1] + temp[j-1][:-1]
            left_direction = 1
        else:
            temp[j-1] = temp[j-1][1:] + temp[j-1][:1]
            left_direction = -1
    data = copy.deepcopy(temp)

ans = 0
for i in range(1, len(data)):
    ans += int(data[i][0]) * (2 ** (i-1))
print(ans)
