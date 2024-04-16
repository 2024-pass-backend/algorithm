def solution(data, col, row_begin, row_end):
    answer = 0
    sort_data = sorted(data, key=lambda x:(x[col-1], -x[0]))
    answer = sum([t%(row_begin) for t in sort_data[row_begin-1]])
    for i in range(row_begin, row_end):
        answer ^= sum([t%(i+1) for t in sort_data[i]])
        
    return answer