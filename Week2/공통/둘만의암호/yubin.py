from string import ascii_lowercase

def solution(s, skip, index):
    alph = set(ascii_lowercase)
    alph -= set(skip)
    sorted_alph = sorted(alph)
    
    res = []
    for s_i in s:
        idx = sorted_alph.index(s_i)+index
        while idx >= len(sorted_alph):
            idx -= len(sorted_alph)
            
        res.append(sorted_alph[idx])
    return ''.join(res)