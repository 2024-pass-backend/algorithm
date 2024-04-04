def solution(board):
    def isEqual(v, x):
        return all(i == v for i in x)

    board = [list(b) for b in board]
    board2 = list(map(list, zip(*board)))

    # O 빙고 갯수, X 빙고 갯수, O 총 갯수, X 총 갯수, 왼위, 오아 대각선, 반대 대각선 리스트
    o_cnt, x_cnt, o, x, cross1, cross2 = 0, 0, 0, 0, [], []

    # O 빙고 갯수, X 빙고 갯수 계산
    for b in board:
        if isEqual("O", b):
            o_cnt += 1
        if isEqual("X", b):
            x_cnt += 1

    # 전치 행렬의 O 빙고 갯수, X 빙고 갯수 계산
    for b in board2:
        if isEqual("O", b):
            o_cnt += 1
        if isEqual("X", b):
            x_cnt += 1

    # 대각선 원소들 리스트에 넣음
    for i in range(3):
        cross1.append(board[i][i])
        cross2.append(board[i][2 - i])

    # 대각선 빙고 갯수 계산
    o_cnt += 1 if isEqual("O",cross1) else 0
    o_cnt += 1 if isEqual("O",cross2) else 0
    x_cnt += 1 if isEqual("X",cross1) else 0
    x_cnt += 1 if isEqual("X",cross2) else 0

    # O의 총 갯수, X의 총 갯수 계산
    for r in board:
        for c in r:
            if c == "O":
                o += 1
            if c == "X":
                x += 1

    # 틱택토에서 승리하는 빙고의 갯수 조건
    a = o_cnt == 0 and x_cnt == 0
    b = o_cnt == 1 and x_cnt == 0
    c = o_cnt == 0 and x_cnt == 1
    d = o_cnt == 2 and x_cnt == 0

    if a and o in (x, x + 1):
        return 1

    if b and o == 4 and x == 3:
        return 1

    if c and o == x:
        return 1

    if d and o == 5 and x == 4:
        return 1

    return 0