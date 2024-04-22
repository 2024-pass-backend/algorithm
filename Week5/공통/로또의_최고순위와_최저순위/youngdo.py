def solution(lottos, win_nums):
    min_corr = 0  # 최저 개수
    cnt_zero = 0  # 0 개수
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            min_corr += 1
        if lottos[i] == 0:
            cnt_zero += 1

    total = min_corr + cnt_zero  # 최고 개수

    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}  # 개수에 따른 등수 딕셔너리

    answer = [rank[total], rank[min_corr]]

    return answer