def solution(price, money, count):
    answer = 0
    
    sum1 = 0
    
    for i in range(1, count+1) :
        sum1 = sum1 + (price * i)
        
    answer = sum1 - money
    
    if answer <= 0 :
        answer = 0
    

    return answer