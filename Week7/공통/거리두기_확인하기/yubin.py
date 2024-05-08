from itertools import combinations
def solution(places):
    answer = []
    # manhatan distance
    def manhatan(c1, c2):
        return abs(c1[0]-c2[0])+abs(c1[1]-c2[1])
    
    for place in places:
        res = 1
        P_list = []
        for r in range(5):
            for c in range(5):
                if place[r][c]=='P':
                    P_list.append([r, c])
        
        cb = combinations(P_list, 2)
        for p1, p2 in cb:
            # 거리 2이하
            if manhatan(p1, p2)<=2:
                # r 동일
                if p1[0]==p2[0]:
                    temp_c = min(p1[1], p2[1])
                    if place[p1[0]][temp_c+1]!='X':
                        res = 0
                        break
                elif p1[1]==p2[1]:
                    temp_r = min(p1[0], p2[0])
                    if place[temp_r+1][p1[1]]!='X':
                        res = 0
                        break
                else:
                    if place[p1[0]][p2[1]]!='X' or place[p2[0]][p1[1]]!='X':
                        res = 0
                        break
        answer.append(res)
    return answer