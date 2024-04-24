def solution(numbers, hand):
    answer = []
    left = (3, 0)
    right = (3, 2)
    l_dic = {1:(0, 0), 4:(1, 0), 7:(2, 0)}
    r_dic = {3:(0, 2), 6:(1, 2), 9:(2, 2)}
    mid_dic = {2:(0, 1), 5:(1, 1), 8:(2, 1), 0:(3, 1)}
    
    for n in numbers:
        if n in l_dic.keys():
            left = l_dic[n]
            answer.append('L')
        elif n in r_dic.keys():
            right = r_dic[n]
            answer.append('R')
        else:
            n_coord = mid_dic[n]
            l_dist = abs(n_coord[0]-left[0])+abs(n_coord[1]-left[1])
            r_dist = abs(n_coord[0]-right[0])+abs(n_coord[1]-right[1])
            if l_dist < r_dist:
                left = mid_dic[n]
                answer.append('L')
            elif l_dist > r_dist:
                right = mid_dic[n]
                answer.append('R')
            else:
                if hand=='left':
                    left = mid_dic[n]
                    answer.append('L')
                else:
                    right = mid_dic[n]
                    answer.append('R')
    return ''.join(answer)