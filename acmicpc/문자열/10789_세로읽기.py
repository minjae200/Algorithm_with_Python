array = [input() for _ in range(5)]

index = 0
for j in range(15):
    for i in range(5):
        try:
            print(array[i][index], end='')
        except:
            pass
    index += 1