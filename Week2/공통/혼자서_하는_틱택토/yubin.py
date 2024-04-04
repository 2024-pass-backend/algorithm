def solution(board):
    ttt_dic = {'O':0, 'X':0, '.':0, 1:[], 2:[], 3:[]}
    r1, r2, r3 = set(), set(), set()
    c1, c2, c3 = set(), set(), set()
    d1, d2 = set(), set()
    for i in range(3):
        r1.add(board[0][i])
        r2.add(board[1][i])
        r3.add(board[2][i])
        c1.add(board[i][0])
        c2.add(board[i][1])
        c3.add(board[i][2])
        d1.add(board[i][i])
        d2.add(board[2-i][2-i])
        for j in range(3):
            ttt_dic[board[i][j]]+=1
    
    ttt = [r1, r2, r3, c1, c2, c3, d1, d2]
    for t in ttt:
        ttt_dic[len(t)].append(t)
    
    # 표시 실수
    if (ttt_dic['O']!=ttt_dic['X']) and (ttt_dic['O']!=ttt_dic['X']+1):
        return 0
    
    # 이미 끝났는데도 더 둠
    if len(ttt_dic[1])>0:
        if (ttt_dic[1][0] == set(['O'])) & (ttt_dic['O']!=ttt_dic['X']+1):
            return 0
        elif (ttt_dic[1][0] == set(['X'])) & (ttt_dic['O']!=ttt_dic['X']):
            return 0
    return 1