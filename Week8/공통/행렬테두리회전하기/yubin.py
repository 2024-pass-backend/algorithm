from collections import deque
def solution(rows, columns, queries):
    def margin(matrix, query):
        r1, c1, r2, c2 = query
        
        coord = []
        values = deque([])
        min_val = 10001
        
        # 상
        for c in range(c1, c2):
            coord.append((r1, c))
            v = matrix[r1][c]
            values.append(v)
            min_val = min(min_val, v)
        # 우
        for r in range(r1, r2):
            coord.append((r, c2))
            v = matrix[r][c2]
            values.append(v)
            min_val = min(min_val, v)
        # 하
        for c in range(c2, c1, -1):
            coord.append((r2, c))
            v = matrix[r2][c]
            values.append(v)
            min_val = min(min_val, v)
        # 좌
        for r in range(r2, r1, -1):
            coord.append((r, c1))
            v = matrix[r][c1]
            values.append(v)
            min_val = min(min_val, v)
        return coord, values, min_val
    
    def rotate_margin(matrix, coord, values):
        values.rotate(1)
        for (r, c), v in zip(coord, values):
            matrix[r][c] = v
        return matrix
        
    answer = []
    mat = [[(i-1)*columns+j for j in range(columns+1)] for i in range(rows+1)]
    for q in queries:
        coord, values, min_val = margin(mat, q)
        mat = rotate_margin(mat, coord, values)
        answer.append(min_val)
    return answer