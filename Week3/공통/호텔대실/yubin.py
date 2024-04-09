def solution(book_time):
    answer = 0
    # 단위 환산
    book_list = []
    for start, end in book_time:
        temp = [0, 0]
        temp[0] = int(start[:2])*60+int(start[-2:])
        temp[1] = int(end[:2])*60+int(end[-2:]) + 10 # 청소시간 포함
        book_list.append(temp)
    
    # 정렬
    book_list.sort()
    
    room = []
    for book in book_list:
        # 방 없는 경우
        if len(room)==0:
            # 사용 종료 시간 추가
            room.append(book[1])
        # 방 있고, 그 방 사용할 수 있는 경우
        elif room[0] <= book[0]:
            room[0] = book[1]
        # 방은 있는데 아직 앞사람 사용중
        elif room[0] > book[0]:
            room.append(book[1])
        room.sort()
    return len(room)