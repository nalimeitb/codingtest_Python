def solution(left, right):
    answer = 0
    
    for i in range(left, right+1) :
        count = 0
        for k in range(1, i+1) :
            if i % k == 0 :
                count = count + 1
                
        if count % 2 == 0 :
            answer = answer + i
        else :
            answer = answer - i
    
    return answer