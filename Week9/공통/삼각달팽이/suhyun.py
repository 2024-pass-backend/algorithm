# sum (2차원배열, [])
# 2차원배열을 순회하면서 []리스트에 값을 채워준다.
# answer = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# 라고 할때, 반환값은 [1, 2, 3, 4, 5, 6, 7, 8, 9]가 된다.
# https://developnote.tistory.com/26
def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]
    # print(answer)
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
    return sum(answer, [])

print(solution(5))