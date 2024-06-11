def solution(nums):
    N = len(nums)
    kind_n = len(set(nums))
    answer = min(N//2, kind_n)
    return answer