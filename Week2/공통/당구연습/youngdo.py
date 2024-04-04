def solution(m, n, startX, startY, balls):
    answer=[]
    for ball in balls:
        x, y = ball[0], ball[1]
        if x == startX:
            if y > startY :
                answer.append(min((startY+y)**2,(y-startY)**2+4*min(x,m-x)**2))
            else:
                answer.append(min((2*n-startY-y)**2,(y-startY)**2+4*min(x,m-x)**2))
        elif y == startY:
            if x > startX:
                answer.append(min((startX+x)**2,(x-startX)**2+4*min(y,n-y)**2))
            else:
                answer.append(min((2*m-startX-x)**2,(x-startX)**2+4*min(y,n-y)**2))
        else:
            answer.append(min((x-startX)**2+min(startY+y,2*n-startY-y)**2,(y-startY)**2+min(startX+x,2*m-startX-x)**2))
    return answer