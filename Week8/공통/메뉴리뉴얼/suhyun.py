# 8:05 ~ 9:27 (음..) 만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
# 저 조건 때문에 틀린 코드가 되는데 어떻게 함..?
# 문자열을 sorted하면 리스트로 반환이 된다.
# s = 'adfe' -> sorted(s) -> ['a', 'd', 'e', 'f']
# ''.join(sorted(s)) -> adef
# 틀린 코드
from itertools import combinations
def solution(orders, course):
    answer = []
    
    total = dict()
    people_val = dict()
    people = dict() # [1번 : [x, y, z]]
    
    for i, o in enumerate(orders):
        for menu in o:
            if menu in total:
                total[menu] = total[menu] + 1
            else:
                total[menu] = 1
            if menu in people_val:
                people_val[menu].append(i+1)
            else:
                people_val[menu] = [i+1]
            if (i + 1) in people:
                people[i + 1].append(menu)
            else:
                people[i + 1] = [menu]
        
    print(people_val)
    print(total)
    print(people)
    
    for c in course:
        for person in combinations(range(1, len(orders)), c):
            cnt = 0
            menu = []
            ans = ''
            for p in person:
                for m in people[p]:
                    if m in menu:
                        continue
                    can = True
                    for pp in person:
                        if pp not in people_val[m]:
                            can = False
                            break
                    if can == True:
                        cnt += 1
                        for ppp in person:
                            if ppp in people_val[m]:
                                people_val[m].remove(ppp)
                            if m in people[ppp]:
                                people[ppp].remove(m)
                        menu.append(m)
                        if total[m] - len(person) > 0:
                            total[m] -= len(person)
                    if cnt == c:
                        ans = ''.join(menu)
                        break
                if len(ans) > 0:
                    break
            answer.append(''.join(sorted(ans)))
                       
                    
                
    
    
    return answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))