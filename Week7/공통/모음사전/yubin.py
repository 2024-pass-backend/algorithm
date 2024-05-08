from itertools import product
def solution(word):
    alph = [' ', 'A', 'E', 'I', 'O', 'U']
    cb = product(alph, repeat=5)
    dic = set([])
    for _w in cb:
        w = ''.join(_w).replace(' ', '')
        dic.add(w)
    dic = list(dic)
    dic.sort()
    return dic.index(word)