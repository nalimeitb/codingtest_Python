def solution(arr):
    answer = []
    tmp = None
    
    for i in arr :
        if tmp != i :
            answer.append(i)
            tmp = i
        else :
            continue
        
    
    
    
    
    return answer