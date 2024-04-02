def solution(picks, minerals):
    answer = 0
    mineralSort = []

    able = min(sum(picks) * 5, len(minerals))
    dia, iron, stone = 0, 0, 0

    for i in range(able):
        if minerals[i] == 'diamond':
            dia += 1
        elif minerals[i] == 'iron':
            iron += 1
        elif minerals[i] == 'stone':
            stone += 1

        # 5개씩 묶어서 파악, 안되면 가능한거에서 하나뺌
        if (i + 1) % 5 == 0 or i == able - 1:
            mineralSort.append((dia, iron, stone))
            dia, iron, stone = 0, 0, 0

    mineralSort.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

    # 좋은 곡괭이를 먼저 사용
    i = 0
    for dia, iron, stone in mineralSort:
        # 곡괭이 파악
        while picks[i] == 0:
            i += 1

        # 피로도
        if i == 0:
            answer += (dia + iron + stone)
        elif i == 1:
            answer += (dia * 5 + iron + stone)
        elif i == 2:
            answer += (dia * 25 + iron * 5 + stone)

        # 파괴
        picks[i] -= 1

    return answer