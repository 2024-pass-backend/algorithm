import sys

def solution(sequence, k):
    answer = []
    R, sum, ans, first, second = 0, 0, sys.maxsize, 0, 0
    for L in range(0, len(sequence)):
        while(sum < k and R < len(sequence)):
            sum += sequence[R]
            R += 1
        
        if sum >= k:
            if sum == k and ans > R - L:
                first = L
                second = R - 1
            ans = min(ans, R - L)
            sum -= sequence[L]
    
    answer.append(first)
    answer.append(second)        
    return answer

sequence = [1, 2, 3, 4, 5]
print(solution(sequence, 7))