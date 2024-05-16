from collections import deque
def solution(arr):
    def SplitArr(in_arr):
        split_arr = [[], [], [], []]
        for r in range(len(in_arr)):
            row = in_arr[r]
            if r<len(in_arr)//2:
                split_arr[0].append(row[:len(in_arr)//2])
                split_arr[1].append(row[len(in_arr)//2:])
            else:
                split_arr[2].append(row[:len(in_arr)//2])
                split_arr[3].append(row[len(in_arr)//2:])
        return split_arr
    
    def check(in_arr):
        flatten = sum(in_arr, [])
        return sum(flatten)==0 or sum(flatten)==len(in_arr)**2
    
    answer = [0, 0] # 0, 1
    
    que = deque([arr])
    while que:
        now_arr = que.popleft()
        if check(now_arr):
            answer[now_arr[0][0]]+=1
        else:
            split_arr = SplitArr(now_arr)
            for sa in split_arr:
                que.append(sa)  

    return answer