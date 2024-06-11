def solution(s):
    med_idx, r = divmod(len(s), 2)
    print(med_idx, r)
    if r:
        return s[med_idx]
    return s[med_idx-1:med_idx+1]