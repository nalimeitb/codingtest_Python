def solution(n):
    answer = []
    
    while True :
        answer.append(n)
        if n != 1 :
            if n % 2 == 0 :
                n = n / 2
            else :
                n = 3 * n + 1
        elif n == 1 :
            break
            
        
    
    return answer