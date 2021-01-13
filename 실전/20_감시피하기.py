from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []
for i in range(n):
    board.append(list(map(str, input().split())))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i,j))
        elif board[i][j] == 'X':
            spaces.append((i,j))


def watch(x, y, dir):
    if dir == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            y -= 1
    elif dir == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            y += 1
    elif dir == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            x -= 1
    elif dir == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            elif board[x][y] == 'O':
                return False
            x += 1

def found_student():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False
for data in list(combinations(spaces, 3)):
    for x, y in data:
        board[x][y] = 'O'
    
    find = True if not found_student() else False
    if find:
        break

    for x, y in data:
        board[x][y] = 'X'

print("YES") if find else print("NO")

"""
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
YES
4
S S S T
X X X X
X X X X
T T T X
"""