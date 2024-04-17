def solution(X, Y):
    answer = ''
    ans = []
    
    z = False
    for k in range(10):
        if str(k) in X and str(k) in Y:
            z = True
            if Y.count(str(k)) > 1 or X.count(str(k)) > 1:
                cnt = min(Y.count(str(k)), X.count(str(k)))
                for _ in range(cnt):
                    ans.append(str(k))
            else:
                ans.append(str(k))
            # print(str(k))
            # print(X.count(str(k)))
            # print(Y.count(str(k)))
            # print("=====")
    
    ans.sort(reverse=True)
    if z == False:
        answer = "-1"
    
    # print(ans)
    for a in ans:
        answer += a
    
    if len(answer) > 1 and answer[0] == "0":
        answer = "0"
    
    return answer

print(solution("1000", "100"))