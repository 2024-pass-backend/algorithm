## 52 ~ 10:03
def solution(name, yearning, photo):
    answer = []
    
    grade = {} ## {이름:그리움점수}
    for i, n in enumerate(name):
        grade[n] = yearning[i]
    
    print(grade)
    
    for arr in photo:
        sum = 0
        for name in arr:
            if name in grade:
                sum += grade.get(name)
        answer.append(sum)
            
    
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
print(solution(name, yearning, photo))