# 파이썬에서 bin()함수는 정수를 이진수로 변환하는 함수이다.
# bin(5) -> '0b101', 0b는 이진수임을 나타내는 접두사이다.
# 문자열.find(찾으려는 문자 a) -> 가장 왼쪽 끝에 있는 a의 인덱스
# 문자열.rfind(찾으려는 문자 a) -> 가장 오른쪽 끝에 있는 a의 인덱스
# 찾으려는 문자가 없다면 -> -1반환
# 문자열을 2진수로 해석하여 십진수로 반환해라. -> int(문자열, 2)
def solution(numbers):
    answer = []
    
    for n in numbers:
        if n % 2 == 0:
            answer.append(n + 1)
        else:
            temp = '0' + bin(n)[2:]
            right_idx = temp.rfind('0')
            temp_list = list(temp)
            
            temp_list[right_idx] = '1'
            temp_list[right_idx + 1] = '0'
            
            temp_str = ''.join(temp_list)
            
            answer.append(int(temp_str, 2))
    return answer

print(solution([7]))