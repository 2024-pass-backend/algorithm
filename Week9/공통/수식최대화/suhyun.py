#import re, re.split(r'구분하려는문자|구분하려는문자', 특정문자열)
# 문자열.find(찾는문자) > 찾는 문자가 없다면 -1반환
# 리스트.insert(인덱스, 원소) > 특정 인덱스에 원소 삽입
# 문자열.find(찾는 문자) 문자열.index(찾는 문자), 둘다 찾는 문자의 인덱스를 반환하지만 리스트.index(찾는문자)는 찾는 문자가 없을시 에러반환
# 리스트에서 특정 원소의 인덱스를 반환하려면, find는 없고 index만있음. 마찬가지로, 찾는 원소가 없다면 에러 반환
# 리스트.pop(인덱스), 리스트.remove(값)
import re, copy
from itertools import permutations
answer = -1e9
def solution(expression):
    operator = set()
    ex_real = list()
    for ex in expression:
        if ex in ['-', '*', '+']:
            operator.add(ex)
            ex_real.append(ex)
    
    for oper in permutations(list(operator), len(operator)):
        print(oper)
        nums = re.split(r'-|\*|\+', expression)
        operator_real = copy.deepcopy(ex_real)
        while len(nums) > 1:
            for op in oper:
                while True:
                    if op not in operator_real:
                        break
                    else:
                        if op in operator_real:
                            idx = operator_real.index(op)
                            operand1 = nums[operator_real.index(op)]
                            operand2 = nums[operator_real.index(op) + 1]
                        if op == '-':
                            val = int(operand1) - int(operand2)
                        elif op == '*':
                            val = int(operand1) * int(operand2)
                        else:
                            val = int(operand1) + int(operand2)
                        if op in operator_real:
                            operator_real.remove(op)
                        if operand1 in nums:
                            nums.insert(idx, val)
                            nums.pop(idx + 1)
                        if operand2 in nums:
                            nums.pop(idx + 1)
        global answer
        answer = max(answer, abs(int(nums[0])))
        
    return answer

# print(solution("100-200*300-500+20"))
print(solution("2-990-5+2"))