def solution(arr, k):
    answer = []
    
    if k % 2 != 0 :
        for i in range(len(arr)) :
            arr[i] = arr[i] * k
    else :
        for i in range(len(arr)) :
            arr[i] = arr[i] + k
            
    answer = arr
    
    return answer