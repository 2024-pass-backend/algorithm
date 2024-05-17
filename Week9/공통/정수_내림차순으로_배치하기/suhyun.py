# 문자열을 정렬하고 싶을땐, 문자열.sort()는 없고, sorted(문자열)로 가능하다.
# 단, 반환값은 리스트이다.
# sorted로 내림차순 정렬하고 싶을땐, sorted(문자열, reverse=True)
# 배열.sort(reverse=True)
def solution(n):
    array = sorted(str(n), reverse=True)
    answer = ''.join(array)
    return int(answer)

print(solution(118372))