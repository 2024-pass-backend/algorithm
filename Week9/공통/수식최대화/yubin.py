from itertools import permutations
def solution(expression):
    answer = 0
    cal = ["*", "-", "+"]
    for c in permutations(cal):
        last_cal = expression.split(c[0])
        second_cal = [l.split(c[1]) for l in last_cal]
        for idx3 in range(len(last_cal)):
            part_cal = second_cal[idx3]
            for idx2 in range(len(part_cal)):
                now = part_cal[idx2].split(c[2])
                temp1 = int(now[0])
                if len(now) > 1:
                    for idx1 in range(1, len(now)):
                        if c[2]=='+':
                            temp1 += int(now[idx1])
                        elif c[2]=='-':
                            temp1 -= int(now[idx1])
                        else:
                            temp1 *= int(now[idx1])
                if idx2 == 0:
                    temp2 = temp1
                else:
                    if c[1]=='+':
                        temp2+=temp1
                    elif c[1]=='-':
                        temp2-=temp1
                    else:
                        temp2*=temp1
            if idx3==0:
                temp3 = temp2
            else:
                if c[0]=='+':
                    temp3 += temp2
                elif c[0]=='-':
                    temp3 -= temp2
                else:
                    temp3 *= temp2
        answer = max(answer, abs(temp3))
    return answer