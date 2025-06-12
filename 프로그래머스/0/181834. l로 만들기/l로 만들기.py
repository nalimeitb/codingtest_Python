def solution(myString):
    answer = ''
    
    for i in range(len(myString)) :
        if myString[i] < 'l' :
            answer = answer + 'l'
        else :
            answer = answer + myString[i]
        
    
    return answer