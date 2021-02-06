n, m, x, y, k = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
#        동 서  북 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

dice = [0] * 7

def dice_move(direction):
    if direction == 1:
        dice[1], dice[6], dice[4], dice[3] = dice[3], dice[4], dice[1], dice[6]
    elif direction == 2:
        dice[1], dice[6], dice[4], dice[3] = dice[4], dice[3], dice[6], dice[1]
    elif direction == 3:
        dice[1], dice[5], dice[2], dice[6] = dice[2], dice[1], dice[6], dice[5]
    elif direction == 4:
        dice[1], dice[5], dice[2], dice[6] = dice[5], dice[6], dice[1], dice[2]

command = list(map(int, input().split()))
for i in command:
    x = x + dx[i]
    y = y + dy[i]
    if 0 > x or 0 > y or n <= x or m <= y:
        x = x - dx[i]
        y = y - dy[i]
        continue
    dice_move(i)
    if board[x][y] == 0:
        board[x][y] = dice[6]
    else:
        dice[6] = board[x][y]
        board[x][y] = 0
    print(dice[1])
