import heapq
def solution(n, k, enemy):
    if len(enemy) <= k:
        return len(enemy)
    
    mjk = enemy[:k]
    heapq.heapify(mjk)
    normal = [0, 0] # sum, cnt
    for e_i in range(k, len(enemy)):
        if enemy[e_i] > mjk[0]:
            normal[0] += heapq.heapreplace(mjk, enemy[e_i])
            normal[1] += 1
        else:
            normal[0] += enemy[e_i]
            normal[1] += 1
            
        if normal[0]==n:
            return normal[1]+k
        if normal[0]>n:
            return normal[1]+k-1
    return len(enemy)
    