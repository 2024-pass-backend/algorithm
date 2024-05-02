def solution(n, k):
    answer = 0
    # 소수 판별
    def isPrime(num):
        if num==1:
            return False
        
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    
    # 진수 계산 (3**13=1,594,323)
    k_form = []
    Flag = False
    for i in range(12, -1, -1):
        if Flag==False and n>=k**i:
            Flag = True
        if Flag:
            q, r = divmod(n, k**i)
            k_form.append(str(q))
            n = r
            
    P_list = ''.join(k_form).split('0')
    for p in P_list:
        if p=='':
            continue
        ip = int(p)
        # print(ip)
        if isPrime(ip):
            answer += 1
    return answer