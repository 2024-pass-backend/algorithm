def solution(array, commands):
    answer = []
    for n in range(len(commands)):
        i, j, k = commands[n]
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer