def solution(board, moves):
    answer = 0
    stack = []
    
    for m in moves:
        for depth in range(len(board)):
            if board[depth][m-1]==0:
                continue
            else:
                doll = board[depth][m-1]
                if len(stack)>0 and stack[-1]==doll:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(doll)
                board[depth][m-1]=0
                break
                
    return answer