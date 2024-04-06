import heapq
def solution(k, score):
    answer = []
    heap = []
    
    for current_score in score:
        if len(heap) == k:
            if heap[0] < current_score:
                heapq.heappop(heap)
        
        if len(heap) < k:
            heapq.heappush(heap, current_score)
        
        answer.append(heap[0])
        
    return answer

score = [10, 100, 20, 150, 1, 100, 200]
print(solution(3, score))