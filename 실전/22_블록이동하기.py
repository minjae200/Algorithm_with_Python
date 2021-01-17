# https://programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

def get_possible_position(board, left, right):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    possible_position = []
    # 상 좌 하 우
    for i in range(4):
        nlx, nly = left[0] + dx[i], left[1] + dy[i]
        nrx, nry = right[0] + dx[i], right[1] + dy[i]
        if board[nlx][nly] == 0 and board[nrx][nry] == 0:
            possible_position.append({(nlx, nly), (nrx, nry)})

    if left[0] == right[0]: # 가로로 있을 때
        if board[left[0]-1][left[1]] == 0 and board[right[0]-1][right[1]] == 0: # 위로 회전 가능한지 체크
            possible_position.append({left, (left[0]-1, left[1])})
            possible_position.append({right, (right[0]-1, right[1])})
        if board[left[0]+1][left[1]] == 0 and board[right[0]+1][right[1]] == 0:
            possible_position.append({left, (left[0]+1, left[1])})
            possible_position.append({right, (right[0]+1, right[1])})
    elif left[1] == right[1]: # 세로로 있을 때
        if board[left[0]][left[1]+1] == 0 and board[right[0]][right[1]+1] == 0: # 오른쪽 회전 가능한지 체크
            possible_position.append({left, (left[0], left[1]+1)})
            possible_position.append({right, (right[0], right[1]+1)})
        if board[left[0]][left[1]-1] == 0 and board[right[0]][right[1]-1] == 0:
            possible_position.append({left, (left[0], left[1]-1)})
            possible_position.append({right, (right[0], right[1]-1)})
                
    return possible_position

def solution(board):
    q = deque()
    N = len(board)

    new_board = [[1] * (N+2) for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]

    q.append(({(1,1), (1,2)}, 0))
    visited = [{(1,1), (1,2)}]
    
    while q:
        pos, cost = q.popleft()
        if (N, N) in pos:
            return cost
        lwing, rwing = pos
        for position in get_possible_position(new_board, lwing, rwing):
            nlwing, nrwing = position
            if {nlwing, nrwing} in visited: continue
            visited.append({nlwing, nrwing})
            q.append(({nlwing, nrwing}, cost+1))
    return 0


if __name__ == '__main__':
    a = [[0,0,0,1,1], [0,0,0,1,0], [0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]
    b = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]
    c = [[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0]]
    d = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0]]
    e = [[0, 0, 0, 0, 1, 0], [0, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    print(solution(c))
    print(solution(d))
    print(solution(e))
