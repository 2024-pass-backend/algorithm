# 알아볼 수 없는 번호가 0이라고 할때, 0의 개수로 최저순위와 최고순위를 결정한다.
def solution(lottos, win_nums):
    answer = []
    
    a = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    cnt = 0
    #당첨번호를 맞춘 갯수
    for w in win_nums:
        if w in lottos:
            cnt += 1
            
    answer.append(a[cnt])
    
    if 0 in lottos:
        cnt += lottos.count(0)
    
    answer.append(a[cnt])
    answer.sort()
    
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))