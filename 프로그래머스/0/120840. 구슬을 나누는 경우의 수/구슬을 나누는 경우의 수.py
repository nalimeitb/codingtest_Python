def solution(balls, share):
    answer = 1
    gop = balls
    i = 0
    
    while True :
        if balls == share :
            answer = 1
            break
        i = i + 1
        answer = answer * gop / i
        gop = gop - 1
        if i == balls - share :
            break
        else :
            continue
    
    return answer