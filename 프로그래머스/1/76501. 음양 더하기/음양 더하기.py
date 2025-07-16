def solution(absolutes, signs):
    answer = 0
    
    for x, y in zip(absolutes, signs) :
        if y == True :
            answer = answer + x
        else :
            answer = answer - x
    
    return answer