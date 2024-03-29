def solution(players, callings):
    answer = [0] * len(players)
    rank = {} ## {등수:이름}
    rank2 = {} ## {이름:등수}
    
    for i, player in enumerate(players):
        rank[i] = player
        rank2[player] = i
    
    for runner in callings:
        current_ruuner = runner
        current_runner_rank = rank2.get(current_ruuner)
        prev_runner = rank.get(current_runner_rank - 1)
        
        rank2[current_ruuner] = current_runner_rank - 1
        rank[current_runner_rank - 1] = current_ruuner
        
        rank2[prev_runner] = current_runner_rank
        rank[current_runner_rank] = prev_runner
    
    for i, player in enumerate(players):
        answer[i] = rank.get(i)
        
    return answer

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

print(solution(players, callings))