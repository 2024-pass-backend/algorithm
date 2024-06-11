def solution(a, b):
    answer = ''
    day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['THU','FRI','SAT', 'SUN','MON','TUE','WED']
    
    d = sum(day_list[:a-1])+b
    
    return days[d%7]