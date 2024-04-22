def solution(lottos, win_nums):
    correct = 0
    zeros = 0
    win_nums = set(win_nums)
    for l in lottos:
        if l in win_nums:
            correct += 1
            win_nums.remove(l)
        elif l==0:
            zeros += 1
            
    return [min(6, 7-correct-zeros), min(6, 7-correct)]