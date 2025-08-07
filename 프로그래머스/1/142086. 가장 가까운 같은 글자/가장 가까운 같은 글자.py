def solution(s):
    answer = []
    
    answer.append(-1)
    
    for i in range(1, len(s)) :
        for k in range(i-1, -1, -1) :
            if s[i] == s[k] :
                answer.append(i-k)
                break
        else :
            answer.append(-1)
            
    return answer