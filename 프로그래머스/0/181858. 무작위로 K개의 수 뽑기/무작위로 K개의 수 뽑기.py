def solution(arr, k):
    answer = []
    
    for i in arr :
        if len(answer) < k :
            if i not in answer :
                answer.append(i)
            
    if len(answer) < k :
        for j in range(0,k-len(answer)) :
            answer.append(-1)
        
    return answer