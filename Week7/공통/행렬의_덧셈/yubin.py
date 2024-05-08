def solution(arr1, arr2):
    answer = []
    r, c = len(arr1), len(arr1[0])
    for ri in range(r):
        temp = []
        for ci in range(c):
            temp.append(arr1[ri][ci]+arr2[ri][ci])
        answer.append(temp)
    return answer