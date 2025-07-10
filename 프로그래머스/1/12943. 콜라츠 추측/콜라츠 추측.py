def solution(num):
    answer = 0
    a = 0
    
    while num != 1 :
        a = a + 1
            
        if num % 2 == 0 :
            num = int(num/2)
        else :
            num = num * 3 + 1
            
        if num == 1 :
            answer = a
            break
        if a == 500 :
            answer = -1
            break
    
    return answer