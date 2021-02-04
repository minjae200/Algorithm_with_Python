
for _ in range(int(input())):

    M, N, x, y = map(int, input().split())
    find = False
    while x <= M * N:
        if (x - y) % N == 0:
            find = True
            print(x)
            break
        x += M
    if not find: print(-1)
