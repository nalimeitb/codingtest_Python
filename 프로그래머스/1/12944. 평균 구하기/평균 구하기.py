def solution(arr):
    answer = 0
    
    sum1 = 0
    
    for i in arr :
        sum1 = sum1 + i
        
    answer = sum1 / len(arr)
    
    return answer