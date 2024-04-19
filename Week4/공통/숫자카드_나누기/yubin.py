import math
def solution(arrayA, arrayB):
    if set(arrayA).intersection(set(arrayB)): # O(N1+N2)
        return 0

    temp_a = arrayA[0]
    aa = True

    for i in range(1, len(arrayA)):
        temp_a = math.gcd(temp_a, arrayA[i])
        if temp_a == 1:
            break

    for b in arrayB:
        if b%temp_a==0:
            aa = False
            break


    temp_b = arrayB[0]

    for i in range(1, len(arrayB)):
        temp_b = math.gcd(temp_b, arrayB[i])
        if temp_b == 1:
            break

    for a in arrayA:
        if a%temp_b==0:
            if aa:

                return temp_a
            else:
                return 0

    answer = max(temp_a, temp_b)

    return answer