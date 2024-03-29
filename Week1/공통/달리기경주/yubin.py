def solution(players, callings):
    # answer = []
    for call in callings:
        call_i = players.index(call)
        front = players[call_i-1]
        players[call_i-1] = call
        players[call_i] = front
    return players

def solution(players, callings):
    rank1 = {player:i for i, player in enumerate(players)}
    rank2 = {i: player for i, player in enumerate(players)}
    for call in callings:
        rank1[call] -= 1
        front = rank2[rank1[call]]
        rank1[front] += 1
        rank2[rank1[call]] = call
        rank2[rank1[call]+1] = front

    return list(rank2.values())