n = int(input())
k = int(input())

Dummy = [[0] * (n+1) for _ in range(n+1)]
for _ in range(k):
    x, y = map(int, input().split())
    Dummy[x][y] = 1

Rotate = []
l = int(input())
for _ in range(l):
    x, c = input().split()
    Rotate.append((int(x),c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def simulate():
    x, y = 1, 1
    Dummy[x][y] = 2
    direction = 0
    result = 0
    rotCnt = 0
    q = [(x,y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 > nx or 1 > ny or n < nx or n < ny:
            result += 1
            break
        if Dummy[nx][ny] == 2:
            result += 1
            break
        if Dummy[nx][ny] == 1:
            Dummy[nx][ny] = 2
            q.append((nx, ny))
        elif Dummy[nx][ny] == 0:
            px, py = q.pop(0)
            Dummy[px][py] = 0
            Dummy[nx][ny] = 2
            q.append((nx, ny))
        result += 1
        x, y = nx, ny
        if rotCnt >= 0 and Rotate[rotCnt][0] == result:
            if Rotate[rotCnt][1] == 'L':
                direction = (direction - 1) % 4
            elif Rotate[rotCnt][1] == 'D':
                direction = (direction + 1) % 4
            rotCnt += 1
            if rotCnt >= len(Rotate):
                rotCnt = -1

    return result
print(simulate())