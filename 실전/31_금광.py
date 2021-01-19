import copy

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    start = 0
    board = []
    for end in range(n):
        end = (end+1)*m
        board.append(array[start:end])
        start = end
    
    cache = []
    cache = copy.deepcopy(board)
    print(cache)
    for j in range(1, m):
        for i in range(n):
            if j-1 >= 0:
                cache[i][j] = max(cache[i][j], cache[i][j-1] + board[i][j])
            if j-1 >= 0 and i+1 < n:
                cache[i][j] = max(cache[i][j], cache[i+1][j-1] + board[i][j])
            if j-1 >= 0 and i-1 >= 0:
                cache[i][j] = max(cache[i][j], cache[i-1][j-1] + board[i][j])
            

    result = -1
    for i in range(n):
        result = max(result, cache[i][m-1])
    print(result)

"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5  0 2 3 0 6 1 2
"""