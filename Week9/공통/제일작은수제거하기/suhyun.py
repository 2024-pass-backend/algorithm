def solution(arr):
    answer = []
    n = min(arr)
    arr.remove(n)
    return arr if len(arr) > 0 else [-1]

print(solution([10]))