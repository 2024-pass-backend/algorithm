def solution(n, m, section):
    '''
    n: 벽 1미터씩 n개 (1번~n번)
    m: 롤러 길이 m미터
    section: 다시 칠해야하는 구역 
    겹치거나 여러 번 칠해도 되지만 일부만 칠하면 안 됨 벽 벗어나도 안 됨
    '''
    answer = 0
    start = 0
    for sec in section:
        if sec >= start:
            start = sec + m
            answer +=1
            
    return answer