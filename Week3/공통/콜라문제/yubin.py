import sys
sys.setrecursionlimit(10000)

def solution(a, b, n):
    def recursion(now_bottle):
        num_group = now_bottle//a
        remain = now_bottle % a
        # 병 더 얻을 수 없으면 정지
        if num_group == 0:
            return 0
        # 재귀 (새로 받은 콜라+남은 병)
        new = recursion(num_group*b+remain)
        return num_group*b+new
    
    return recursion(n)