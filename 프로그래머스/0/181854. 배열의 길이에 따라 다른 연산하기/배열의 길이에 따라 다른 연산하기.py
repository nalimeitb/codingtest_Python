def solution(arr, n):
    answer = []
    
    for i in range(len(arr)) :
        if len(arr) % 2 != 0 :
            if i % 2 == 0 :
                arr[i] = arr[i] + n
        
        else :
            if i % 2 != 0 :
                arr[i] = arr[i] + n
                
    answer = arr
    
    return answer