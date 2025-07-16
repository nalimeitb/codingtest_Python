def solution(n):
    answer = []
    
    n = str(n)
    n = n[::-1]
    
    answer = list(n)
    
    for i in range(len(answer)) :
        answer[i] = int(answer[i])
    
    return answer