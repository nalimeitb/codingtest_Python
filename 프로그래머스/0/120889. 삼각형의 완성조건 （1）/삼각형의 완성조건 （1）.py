def solution(sides):
    answer = 0
    
    sides = sorted(sides)
    
    if sides[0] + sides[1] > sides[2] :
        answer = 1
    else :
        answer = 2
    
    return answer