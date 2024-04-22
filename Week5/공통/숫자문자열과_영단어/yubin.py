def solution(s):
    answer = []
    num_dic = {'z':(4, 0), 'o':(3, 1), 
               't':{'w': (3, 2), 'h':(5, 3)}, 
               'f':{'o':(4, 4), 'i':(4, 5)}, 
               's':{'i':(3, 6), 'e':(5, 7)},
              'e':(5,8), 'n':(4,9)}
    
    idx = 0
    while idx<len(s):
        if s[idx] in set([str(i) for i in range(10)]):
            answer.append(int(s[idx]))
            idx += 1
        elif s[idx] in set(['t', 'f', 's']):
            answer.append(num_dic[s[idx]][s[idx+1]][1])
            idx += num_dic[s[idx]][s[idx+1]][0]
        else:
            answer.append(num_dic[s[idx]][1])
            idx += num_dic[s[idx]][0]
        
    return int(''.join(map(str, answer)))