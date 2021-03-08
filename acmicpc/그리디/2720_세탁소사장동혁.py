T = int(input())

coins = [25, 10, 5, 1]

for _ in range(T):
    money = int(input())

    index = 0
    while money != 0:
        print(money // coins[index], end=' ')
        money %= coins[index]
        index += 1
    for _ in range(index, len(coins)):
        print(0, end=' ')
    print()