def solution(arr, queries):
    answer = []
    
    for s,e in queries :
        for i in range(s, e+1, 1) :
            arr[i] = arr[i] + 1
            
    answer = arr
    
    return answer