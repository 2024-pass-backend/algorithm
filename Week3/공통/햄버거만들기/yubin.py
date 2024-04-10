def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if len(stack)>3 and stack[-4:]==[1,2,3,1]:
            answer += 1
            for _ in range(4):
                stack.pop()
        
    return answer

def solution_old(ingredient):
    answer = 0
    hamburger = []
    temp = []
    for element in ingredient:
        # 빵 들어옴
        if element == 1:
            # 햄버거 비어있음
            if len(hamburger)==0:
                hamburger.append(1)
            # 햄버거 마지막 덮어야함
            elif hamburger[-1]==3:
                answer+=1
                hamburger = [] # 햄버거 초기화
            # 차례 아님
            else:
                # 햄버거에 내용물 있음
                temp.extend(hamburger)
                hamburger = [element]

        # 야채 들어옴
        elif element == 2:
            # 햄버거에 아무것도 없음
            if len(hamburger)==0:
                # temp에 뭔가 있음
                if temp:
                    # 빵 있음
                    if temp[-1]==1:
                        hamburger.append(temp.pop())
                        hamburger.append(element)
                    # 빵 없음
                    else:
                        temp = []
                # temp에 뭐 없으면 그냥 패스
            # 햄버거에 뭔가 있음
            else:
                # 빵 한 장 있음
                if hamburger[-1]==1:
                    hamburger.append(element)
                # 다른 거 들어가있음
                else:
                    # 망함 다 지우기
                    hamburger = []
                    temp = []
                    
        # 고기 들어옴
        else:
            # 햄버거 비어있음
            if len(hamburger)==0:
                # temp 마지막이 야채임
                if temp:
                    if temp[-1]==2:
                        hamburger = [1,2,3]
                        temp.pop()
                        temp.pop()
                    # 마지막이 야채가 아님 -> 망함 다 지움
                    else:
                        temp = []
            else:
                if hamburger[-1]==2:
                    hamburger.append(element)
                else:
                    hamburger = []
                    temp = []
                
    return answer