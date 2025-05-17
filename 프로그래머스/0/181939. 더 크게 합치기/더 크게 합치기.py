def solution(a, b):
    answer = 0
    a = str(a)
    b = str(b)
    answer1 = a+b
    answer2 = b+a
    if answer1 > answer2 :
        answer = int(answer1)
    else :
        answer = int(answer2)
    return answer