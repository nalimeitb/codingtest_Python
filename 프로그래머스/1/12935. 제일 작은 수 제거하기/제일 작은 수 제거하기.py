def solution(arr):
    answer = []
    
    if len(arr) == 1 :
        answer = [-1]
        
    else :
        arr.remove(min(arr))
        answer = arr
        
    return answer