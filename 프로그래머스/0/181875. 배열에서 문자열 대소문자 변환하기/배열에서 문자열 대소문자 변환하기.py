def solution(strArr):
    answer = []
    
    for i in range(len(strArr)) :
        if i % 2 == 0 :
            strArr[i] = strArr[i].lower()
        else :
            strArr[i] = strArr[i].upper()
            
    answer = strArr
    
    return answer