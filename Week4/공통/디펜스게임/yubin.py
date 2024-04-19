import heapq
def solution(n, k, enemy):
    answer = k
    # k가 라운드보다 클 때
    if k>=len(enemy):
        return len(enemy)
    
    # 무적권 쓸 라운드 적 인원 힙에 저장 (k개)
    k_round = enemy[:k]
    heapq.heapify(k_round)
    
    for r in range(k, len(enemy)):
        answer += 1
        e = heapq.heappushpop(k_round, enemy[r]) # k_round에서 가장 작은값이랑 enemy[r] 비교해서 더 작은 값 반환(pop)
        # 추가되는 애가 더 크면 이전 라운드에서 멈추기
        if e > n:
            return answer-1
        # 그렇지 않으면 answer(라운드 수)에 1 추가
        else:
            n -= e
            if n==0:
                return answer
    return len(enemy)