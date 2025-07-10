def solution(x):
    answer = True
    
    x = str(x)
    sum1 = 0
    
    for i in range(len(x)) :
        sum1 = sum1 + int(x[i])
    
    if int(x) % sum1 == 0 :
        answer = True
    else :
        answer = False
    
    return answer