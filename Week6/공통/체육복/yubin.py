def solution(n, lost, reserve):
    answer = 0
    set_lost = set(lost)
    set_reserve = set(reserve)
    for student in range(1, n+1):
        # 잃어버린 학생인지
        if student in set_lost:
            # 여분 있는지
            if student in set_reserve:
                set_reserve.remove(student)
                answer +=1
            # 여분 없어서 빌려야함
            else:
                if student-1 in set_reserve:
                    set_reserve.remove(student-1)
                    answer += 1
                elif (student+1 in set_reserve) and (student+1 not in set_lost):
                    set_reserve.remove(student+1)
                    answer += 1
        # 안 잃어버림
        else:
            answer +=1
            
    return answer