def solution(phone_number):
    answer = ["*"]*(len(phone_number)-4)
    return "".join(answer)+phone_number[-4:]