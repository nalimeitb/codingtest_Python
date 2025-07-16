def solution(n):
    answer = 0
    a = 1
    
    for i in range(n+1) :
        if n == i**2 :
            a = i+1
            answer = (i+1)**2
            break
            
    if answer != a**2 :
        answer = -1
    
    return answer