def solution(arr1, arr2):
    answer = [[0] * len(arr1[0]) for _ in range(len(arr1))]
    for row in range(len(arr1)):
        for col in range(len(arr1[0])):
            answer[row][col] = arr1[row][col] + arr2[row][col]
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))