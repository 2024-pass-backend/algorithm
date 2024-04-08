def solution(number, limit, power):
    answer = 0

    for n in range(1, number+1):
        nums = 0
        for i in range(1, int(n**0.5)+1):
            if n%i==0:
                if i**2 == n:
                    nums += 1
                else:
                    nums += 2
        
        if nums > limit:
            answer += power
        else:
            answer += nums
    return answer