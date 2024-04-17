def solution(sizes):
    max_w, max_h = 0, 0
    for size in sizes:
        if max(size) > max_w:
            max_w = max(size)
        if min(size) > max_h:
            max_h = min(size)
            
    answer = max_w * max_h
    return answer