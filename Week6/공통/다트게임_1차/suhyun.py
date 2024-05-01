# 구분자가 여러개일 경우, 정규식을 이용한다. import re
# re.split("구분자|구분자", 해당 문자열)
# re.split("구분자|구분자|구분자", 해당문자열)
# 8:54
def solution(dartResult):
    answer = 0
    n = ''
    score = []
    for i in dartResult:
        # 문자열.isnumeric() -> 해당 문자열이 숫자로 이루어져있으면 True
        if i.isnumeric():
            n += i
        elif i == "S":
            n = int(n) ** 1
            score.append(n)
            n = ''
        elif i == "D":
            n = int(n) ** 2
            score.append(n)
            n = ''
        elif i == "T":
            n = int(n) ** 3
            score.append(n)
            n = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == "#":
            score[-1] = score[-1] * -1
    return sum(score)

dartResult = "1D2S#10S"
print(solution(dartResult))