def solution(arr, queries):
    
    answer = []
    alpha = []
    
    for query in queries :
        for j in range(query[0], query[1]+1) :
            if arr[j] > query[2] :
                alpha.append(arr[j])
        if alpha != []:
            answer.append(min(alpha))
            alpha = []
        
        else:   
            answer.append(-1)
            
    return answer