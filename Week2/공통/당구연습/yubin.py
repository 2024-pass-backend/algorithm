def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        tx, ty = ball
        if tx == startX:
            if ty > startY:
                dist = min((startY+ty)**2, (min(startX**2, (m-startX)**2)+(ty-(ty+startY)/2)**2)*4)
            else:
                dist = min((2*m-(startY+ty))**2, (min(startX**2, (m-startX)**2)+(ty-(ty+startY)/2)**2)*4)
        elif ty == startY:
            if tx > startX:
                dist = min((startX+tx)**2, (min(startY**2, (n-startY)**2)+(tx-(tx+startX)/2)**2)*4)
            else:
                dist = min((2*n-(startX+tx))**2, (min(startY**2, (n-startY)**2)+(tx-(tx+startX)/2)**2)*4)
        else:
            dist = min((tx-startX)**2+min(startY+ty,2*n-startY-ty)**2,(ty-startY)**2+min(startX+tx,2*m-startX-tx)**2)
        answer.append(dist)
    return answer