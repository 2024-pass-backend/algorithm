from collections import defaultdict
def solution(x, y, n):
    answer = 0
    dp = defaultdict(lambda: -1)
    dp[x] = 0
    dp[x*2] = 1
    dp[x*3] = 1
    for i in range(x+1, y+1):
        if dp[i-n]!=-1:
            dp[i] = dp[i-n] + 1
        if (i%3 == 0) and (dp[i//3]!=-1):
            if dp[i]!= -1:
                dp[i] = min(dp[i], dp[i//3]+1)
            else:
                dp[i] = dp[i//3]+1
        if (i%2 == 0) and (dp[i//2]!=-1):
            if dp[i]!=-1:
                dp[i] = min(dp[i], dp[i//2]+1)
            else:
                dp[i] = dp[i//2]+1
    return dp[y]