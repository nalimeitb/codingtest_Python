def solution(arr, queries):
    answer = []
    
    for query in queries :
        for i in range(query[0], query[1]+1) :
            if i % query[2] == 0 :
                arr[i] = arr[i] + 1
                
    answer = arr    
    
    return answer