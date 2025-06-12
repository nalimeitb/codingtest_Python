def solution(n):
    answer = []
    
    for i in range(n) :
        answer.append([])
        for k in range(n) :
            if i == k :
                answer[i].append(1)
            else :
                answer[i].append(0)
    
    return answer