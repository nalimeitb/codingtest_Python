def solution(n, k):
    answer = []
    i = 0
    
    while True :
        i = i + 1
        if i*k <= n :
            answer.append(i*k)
        else :
            break
    
    return answer