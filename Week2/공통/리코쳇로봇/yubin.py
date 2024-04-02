# 재귀 dfs로 풀고 싶은데 구현을 못 하겠음
def solution(board):
    answer = 0
    gx, gy = (3, 1)
    h, w = len(board), len(board[0])
    direc_dic = {'up':(0, -1), 'down':(0, 1), 'left':(-1, 0), 'right':(1, 0)}
    
    def move(rx, ry, direction):
        nx, ny = rx, ry
        while True:
            tx, ty = nx, ny
            tx += direc_dic[direction][0]
            ty += direc_dic[direction][1]
            
            # 경계
            if (tx<0) or (ty<0) or (tx>=w) or (tx>=h):
                return nx, ny
            # 장애물
            if board[ty][tx] == 'D':
                return nx, ny
            
            nx, ny = tx, ty
    
    def dfs(stack, depth=1):
        print(stack, depth)
        # 더 이상 수행할 것 없음
        if len(stack)==0:
            
            return 
        
        rx, ry = stack.pop()
        temp_stack = set([])
        for d in direc_dic.keys():
            dx, dy = move(rx, ry, d)
            if dx==gx and dy==gy:
                return depth
            temp_stack.add((dx, dy))
        stack.extend(temp_stack)
        
        dfs(stack, depth+1)
    
    dfs([(6, 0)])
        
    return answer
