def solution(n):
    answer = 0
    
    for i in range(1, n+1) :
        a = 0
        a = n / (i**2)
        if a == 1 :
            answer = 1
            break
        else :
            answer = 2
            
    
    return answer