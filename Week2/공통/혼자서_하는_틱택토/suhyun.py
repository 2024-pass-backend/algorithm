def won(board, t):
    for row in board:
        if row == [t, t, t]:
            return True
        
    for col in range(3):
        if [board[row][col] for row in range(3)] == [t, t, t]:
            return True
    
    if [board[0][0], board[1][1], board[2][2]] == [t, t, t]:
        return True
    if [board[2][0], board[1][1], board[0][2]] == [t, t, t]:
        return True
    return False

def solution(board):
    board = [list(row) for row in board]
    
    o_cnt, x_cnt = 0, 0
    for row in board:
        for c in row:
            if c == 'O':
                o_cnt += 1
            if c == 'X':
                x_cnt += 1
    
    if not (o_cnt == x_cnt or o_cnt == x_cnt + 1):
        return 0
    
    if won(board, 'O') and won(board, 'X'):
        return 0
    
    if won(board, 'O') and o_cnt != x_cnt + 1:
        return 0
    
    if won(board, 'X') and o_cnt != x_cnt:
        return 0
    
    return 1

board = ["O.X", ".O.", "..X"]
print(solution(board))