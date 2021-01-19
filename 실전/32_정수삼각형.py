n = int(input())
board = []

for i in range(n):
    board.append(list(map(int, input().split())))

import copy
cache = copy.deepcopy(board)
for i in range(1, n):
    for j in range(i+1):
        # cache[1][0] , cache[1][1]
        if i-1 >= 0 and j != i:
            cache[i][j] = max(cache[i][j], cache[i-1][j] + board[i][j])
        if i-1 >= 0 and j-1 >= 0:
            cache[i][j] = max(cache[i][j], cache[i-1][j-1] + board[i][j])
result = 0
for i in range(n):
    result = max(result, cache[n-1][i])
print(result)

"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""