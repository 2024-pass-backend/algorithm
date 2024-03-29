## 시간 복잡도= calling*players=> 시간초과
# def solution(players, callings):
#     for i in callings:
#         idx=players.index(i)
#         #인덱스 뒤집기
#         players[idx-1], players[idx] = players[idx], players[idx-1]
#     return players

#딕셔너리로 탐색속도 O(1)
def solution(players, callings):
    player_dict = {player: idx for idx, player in enumerate(players)}
    for call in callings:
        idx = player_dict[call]

        players[idx], players[idx - 1] = players[idx - 1], players[idx]

        player_dict[players[idx]] = idx
        player_dict[players[idx - 1]] = idx - 1
    return players
