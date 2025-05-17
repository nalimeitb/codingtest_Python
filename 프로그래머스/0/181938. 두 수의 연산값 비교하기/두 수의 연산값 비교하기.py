def solution(a, b):
    answer = 0
    a1 = str(a)
    b1 = str(b)
    
    answer1 = int(a1 + b1)
    answer2 = 2*a*b
    
    if answer1 > answer2 :
        answer = answer1
    else :
        answer = answer2
    return answer