# 3:51 ~ 
# Hint : 1부터 0까지 좌표를 저장하는 딕셔너리를 선언한다.

pad = {
    '1' : (0,0), 
    '2' : (0,1),
    '3' : (0,2),
    '4' : (1,0),
    '5' : (1,1),
    '6' : (1,2),
    '7' : (2,0),
    '8' : (2,1),
    '9' : (2,2),
    '0' : (3,1),
    '*' : (3,0),
    '#' : (3,2)
}

def solution(numbers, hand):
    answer = ''
    
    left = pad['*']
    right = pad['#']
    
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left = pad[str(n)]
        if n in [3, 6, 9]:
            answer += 'R'
            right = pad[str(n)]
        if n in [2,5,8,0]:
            L1 = abs(pad[str(n)][0] - left[0]) + abs(pad[str(n)][1] - left[1])
            R1 = abs(pad[str(n)][0] - right[0]) + abs(pad[str(n)][1] - right[1])
            if L1 == R1:
                if hand == "right":
                    right = pad[str(n)]
                    answer += "R"
                else:
                    left = pad[str(n)]
                    answer += "L"
            elif L1 > R1:
                answer += "R"
                right = pad[str(n)]
            else:
                answer += "L"
                left = pad[str(n)]
    return answer

numbers = [0,0]
hand = "right"
print(solution(numbers, hand))