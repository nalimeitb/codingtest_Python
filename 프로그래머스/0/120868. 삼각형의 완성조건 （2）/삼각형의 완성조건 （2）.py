def solution(sides):
    answer = 0
    i = 0
    tmp1 = max(sides) - min(sides)
    tmp2 = max(sides) + min(sides) - 1
    
    while True :
        tmp1 = tmp1 + 1
        answer = answer + 1
        if tmp1 == max(sides) :
            break
            
    while tmp2 > max(sides) :
        tmp2 = tmp2 -1
        answer = answer + 1
    
    return answer